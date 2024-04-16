"""Module for the main class for the module."""

import logging
import os
import random

import numpy as np
from scipy.stats import halfnorm
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

from soil_moisture_prediction.areaGeometry import RectGeom
from soil_moisture_prediction.inputData import InputData
from soil_moisture_prediction.plot_functions import plot_selection

# TODO define private and public attribues and methods

logger = logging.getLogger(__name__)

RANDOM_SEED = 46
random.seed(RANDOM_SEED)


class RFoModel(object):
    """Class to store the output of the Random Forest regression.

    Support deterministic and probabilistic (Monte Carlo) predictions
    """

    random_forest_models = []
    n_trees = 40
    tree_depth = 8
    RF_prediction = np.empty(())
    predictor_importance = np.empty(())
    past_prediction_as_feature = False
    average_measurements_over_time = False
    rain_time_serie = ""
    monte_carlo = False
    MC_mean = np.empty(())
    p5 = np.empty(())
    p25 = np.empty(())
    p75 = np.empty(())
    p95 = np.empty(())
    dispersion_coefficient = np.empty(())

    def __init__(
        self,
        *,
        input_parameters,
        work_dir,
        load_results=False,
    ):
        """Construct."""
        logger.info("Load model")
        self.work_dir = work_dir
        self.rect_geom = RectGeom(input_parameters.geometry)

        predictors_input = {}
        for file_name, predictor_data in input_parameters.predictors.items():
            type_name = predictor_data.type if predictor_data.type != "" else file_name
            if type_name == "rain":
                self.rain_time_serie = os.path.join(self.work_dir, file_name)
            else:
                predictors_input[type_name] = (
                    os.path.join(work_dir, file_name),
                    predictor_data.unit,
                )

        sm_file = [
            file_name for file_name, days in input_parameters.soil_moisture_data.items()
        ][0]
        self.input_data = InputData(
            predictors_input,
            os.path.join(self.work_dir, sm_file),
            self.rect_geom,
            uncertainty=input_parameters.monte_carlo,
        )

        self.monte_carlo = input_parameters.monte_carlo

        if self.monte_carlo:
            self.monte_carlo_iterations = input_parameters.monte_carlo_iterations
        else:
            self.monte_carlo_iterations = 1

        self.past_prediction_as_feature = input_parameters.past_prediction_as_feature
        self.input_data.prepare_predictors(
            self.rect_geom, use_prediction=self.past_prediction_as_feature
        )
        self.average_measurements_over_time = (
            input_parameters.average_measurements_over_time
        )

        if self.past_prediction_as_feature or self.average_measurements_over_time:
            self.reset_when_rain_occurs = False
            if self.rain_time_serie != "":
                self.reset_when_rain_occurs = True

        self.what_to_plot = input_parameters.what_to_plot.model_dump()
        self.save_results = input_parameters.save_results
        if load_results:
            self.load_predictions()
        else:
            self.initiate_result_arrays()

    def initiate_result_arrays(self):
        """Initiate the arrays to store the results."""
        logger.info("Initiating result arrays...")
        self.RF_prediction = np.empty(
            (
                self.monte_carlo_iterations,
                len(self.input_data.soil_moisture_data.start_times),
                self.rect_geom.dim_x,
                self.rect_geom.dim_y,
            )
        )
        if self.monte_carlo:
            shape = (
                len(self.input_data.soil_moisture_data.start_times),
                self.rect_geom.dim_x,
                self.rect_geom.dim_y,
            )
            (
                self.MC_mean,
                self.p5,
                self.p25,
                self.p75,
                self.p95,
                self.dispersion_coefficient,
            ) = [np.empty(shape) for _ in range(6)]
        self.predictor_importance = np.zeros(
            (
                self.monte_carlo_iterations,
                len(self.input_data.soil_moisture_data.start_times),
                self.input_data.number_predictors,
            )
        )

    def compute(self, filter_measurements=False):
        """Build model and make predictions."""
        if self.average_measurements_over_time:
            number_timesteps_for_average = 3
            self.average_measurements(number_timesteps_for_average)

        for time_step, start_time in enumerate(
            self.input_data.soil_moisture_data.start_times
        ):
            self.random_forest_models = []
            if time_step > 0 and self.past_prediction_as_feature:
                self.add_prediction_to_feature(time_step)
            if filter_measurements:
                self.input_data.soil_moisture_filering(start_time)
            self.train_random_forest_models(start_time)
            self.apply_random_forest_models(time_step)
            if self.monte_carlo:
                self.compute_mc_stats(time_step)

        if self.save_results:
            self.save_predictions()

    def average_measurements(self, number_timesteps_for_average):
        """Average soil moisture measurements over the previous days."""
        if (
            len(self.input_data.soil_moisture_data.start_times)
            < number_timesteps_for_average
        ):
            logging.warning(
                "Will not apply average over time intervals. Not enough intervals!"
            )
            return
        soil_moisture_averaged = self.input_data.soil_moisture_data.soil_moisture
        for time_step, start_time in enumerate(
            self.input_data.soil_moisture_data.start_times
        ):
            if time_step > number_timesteps_for_average:
                number_timesteps_rainfall_reset = number_timesteps_for_average
                rain_occurs = False
                if self.reset_when_rain_occurs:
                    rain_occurs = self.input_data.check_rainfall_occurences(
                        number_timesteps_rainfall_reset,
                        time_step,
                        self.rain_time_serie,
                    )
                if not rain_occurs:
                    for past_time_step in range(1, number_timesteps_for_average + 1):
                        past_start_time = (
                            self.input_data.soil_moisture_data.start_times[
                                time_step - past_time_step
                            ]
                        )
                        soil_moisture_averaged[
                            start_time
                        ] += self.input_data.soil_moisture_data.soil_moisture[
                            past_start_time
                        ]
                    soil_moisture_averaged[start_time] /= (
                        number_timesteps_for_average + 1
                    )
        self.input_data.soil_moisture_data.soil_moisture = soil_moisture_averaged

    def add_prediction_to_feature(self, time_step):
        """Add the previous day's prediction to the features."""
        rain_occurs = False
        number_timesteps_rainfall_reset = 1
        if self.reset_when_rain_occurs:
            rain_occurs = self.input_data.check_rainfall_occurences(
                number_timesteps_rainfall_reset,
                time_step,
                self.rain_time_serie,
            )
        if not rain_occurs:
            self.input_data.predictors["past_prediction"] = (
                self.RF_prediction[0, time_step - 1, :, :],
                "g/g",
            )
        else:
            self.input_data.predictors["past_prediction"] = (
                np.zeros((self.rect_geom.dim_x, self.rect_geom.dim_y)),
                "g/g",
            )
        start_time = self.input_data.soil_moisture_data.start_times[time_step]
        self.input_data.set_training_predictors(start_time)

    def train_random_forest_models(self, start_time):
        """Train the random forest models."""
        logger.info(f"[{start_time}] Training Random Forest models...")
        if not self.monte_carlo:
            self.random_forest_models.append(
                self.train_random_forest(
                    self.input_data.training_pred[start_time],
                    self.input_data.soil_moisture_data.soil_moisture[start_time],
                    start_time,
                )
            )
            return

        number_measurements = self.input_data.soil_moisture_data.number_measurements[
            start_time
        ]
        soil_moisture_uncertain = np.empty(
            (self.monte_carlo_iterations, number_measurements)
        )
        for iteration in range(self.monte_carlo_iterations):
            for measurement in range(number_measurements):
                soil_moisture_uncertain[iteration, measurement] = (
                    self.compute_uncertain_soil_moisture(
                        measurement, iteration, start_time
                    )
                )

            self.random_forest_models.append(
                self.train_random_forest(
                    self.input_data.training_pred[start_time],
                    soil_moisture_uncertain[iteration, :],
                    start_time,
                )
            )

    def compute_uncertain_soil_moisture(self, measurement, iteration, start_time):
        """Compute the uncertain soil moisture for the Monte Carlo simulation."""
        soil_moisture = self.input_data.soil_moisture_data.soil_moisture[start_time][
            measurement
        ]
        soil_moisture_dev_low = (
            self.input_data.soil_moisture_data.soil_moisture_dev_low[start_time][
                measurement
            ]
        )
        soil_moisture_dev_high = (
            self.input_data.soil_moisture_data.soil_moisture_dev_high[start_time][
                measurement
            ]
        )

        lower_uncertainty = soil_moisture - float(
            halfnorm.rvs(
                soil_moisture,
                soil_moisture_dev_low,
                1,
                random_state=measurement * 100 + iteration,
            )
        )
        upper_uncertainty = float(
            halfnorm.rvs(
                soil_moisture,
                soil_moisture_dev_high,
                1,
                random_state=measurement * 100 + iteration,
            )
        )

        # TODO This random variable is not effected by the seed. So it is not
        # deterministic.
        # TODO Better variable name than x. Is it longitutde or latitude?
        x = random.randint(0, 1)
        soil_moisture_uncertain = x * lower_uncertainty + (1 - x) * upper_uncertainty
        return soil_moisture_uncertain

    def train_random_forest(self, features, labels, start_time):
        """Build and train a random forest regressor.

        features : training input samples, array-like of shape = [n_samples, n_features]
        labels   : target values (Real soil moisture), array-like, shape = [n_samples]
        """
        # TODO random_state hard coded
        train_features, test_features, train_labels, test_labels = train_test_split(
            features, labels, test_size=0.3, random_state=40
        )
        train_labels = np.ravel(train_labels)
        test_labels = np.ravel(test_labels)

        random_forest = RandomForestRegressor(
            n_estimators=self.n_trees,
            max_depth=self.tree_depth,
            random_state=RANDOM_SEED,
        )
        random_forest.fit(train_features, train_labels)

        predictions = random_forest.predict(test_features)
        r2 = r2_score(test_labels, predictions)
        logger.info(f"[{start_time}] Random Forest R2: {round(r2, 3)}")
        rf_res = predictions - test_labels
        errors = abs(rf_res) ** 2
        mean_absolute_error = round(np.mean(errors), 6)
        logger.info(
            f"[{start_time}] Random Forest Mean Absolute Error: {mean_absolute_error} "
            f"with prediction mean value: {round(np.mean(predictions), 2)}"
        )

        return random_forest

    def apply_random_forest_models(self, time_step):
        """Apply the random forest on the full area and compute feature importance."""
        logger.info(
            f"[{self.input_data.soil_moisture_data.start_times[time_step]}] "
            "Applying Random Forest model(s)..."
        )

        for monte_carlo_iteration in range(self.monte_carlo_iterations):
            for line in range(self.rect_geom.dim_x):
                predictors = np.array(
                    [
                        predictor[0][line, :]
                        for predictor in self.input_data.predictors.values()
                    ]
                ).T
                if self.input_data.apply_pca:
                    predictors = self.input_data.pca.transform(predictors)
                self.RF_prediction[monte_carlo_iteration, time_step, line, :] = (
                    self.random_forest_models[monte_carlo_iteration].predict(predictors)
                )

            if self.input_data.has_mask:
                self.RF_prediction[
                    monte_carlo_iteration, time_step, :, :
                ] *= self.input_data.mask

            self.predictor_importance[monte_carlo_iteration, time_step] = (
                self.random_forest_models[monte_carlo_iteration].feature_importances_
            )

    def compute_mc_stats(self, time_step):
        """Compute mean and percentiles of the prediction for a given day.

        The function computes the 5th, 25th, 75th and 95th percentiles.
        """
        logger.info(f"[{time_step}] Computing Monte Carlo statistics.")

        self.MC_mean[time_step, :, :] = np.mean(
            self.RF_prediction[:, time_step, :, :], axis=0
        )
        (
            self.p5[time_step, :, :],
            self.p25[time_step, :, :],
            self.p75[time_step, :, :],
            self.p95[time_step, :, :],
        ) = [
            np.percentile(self.RF_prediction[:, time_step, :, :], q=perc, axis=0)
            for perc in [5, 25, 75, 95]
        ]
        self.dispersion_coefficient[time_step, :, :] = (
            self.p75[time_step, :, :] - self.p25[time_step, :, :]
        ) / (self.p75[time_step, :, :] + self.p25[time_step, :, :])

    def load_predictions(self):
        """
        Load prediction results and RF feature importance from files.

        If Monte Carlo is switched on, the mean and coefficient of dispersion are also
        loaded.
        """
        logger.info("Loading prediction results from files...")
        self.RF_prediction = np.load(os.path.join(self.work_dir, "RF_predictions.npy"))
        self.predictor_importance = np.load(
            os.path.join(self.work_dir, "RF_feat_importance.npy")
        )
        if self.monte_carlo:
            self.MC_mean = np.load(os.path.join(self.work_dir, "MC_mean.npy"))
            self.dispersion_coefficient = np.load(
                os.path.join(self.work_dir, "MC_coefficient_dispersion.npy")
            )

    def save_predictions(self):
        """
        Save the prediction results and RF feature importance to files.

        If Monte Carlo is switched on, the mean and coefficient of dispersion are also
        saved.
        """
        logger.info("Saving predictions to files...")
        np.save(os.path.join(self.work_dir, "RF_predictions"), self.RF_prediction)
        np.save(
            os.path.join(self.work_dir, "RF_feat_importance"),
            self.predictor_importance,
        )
        if self.monte_carlo:
            np.save(os.path.join(self.work_dir, "MC_mean"), self.MC_mean)
            np.save(
                os.path.join(self.work_dir, "MC_coefficient_dispersion"),
                self.dispersion_coefficient,
            )

    def plot_figure_selection(self):
        """Plot the selected figures."""
        logger.info("Computing selected figures to plot...")
        plot_selection(self)
