"""Pydantic models for the input parameters of the model."""

from typing import Dict, List

from pydantic import BaseModel


class PredictorData(BaseModel):
    """Data model for the predictor data."""

    type: str
    unit: str


class WhatToPlot(BaseModel):
    """Data model for the what to plot data."""

    alldays_predictor_importance: bool
    day_measurements: bool
    day_prediction_map: bool
    day_predictor_importance: bool
    pred_correlation: bool
    predictors: bool


class InputParamaters(BaseModel):
    """Data model for the input parameters."""

    average_measurements_over_time: bool
    geometry: List[int]
    monte_carlo: bool
    monte_carlo_iterations: int
    past_prediction_as_feature: bool
    predictors: Dict[str, PredictorData]
    save_results: bool
    soil_moisture_data: Dict[str, List[str]]
    what_to_plot: WhatToPlot
