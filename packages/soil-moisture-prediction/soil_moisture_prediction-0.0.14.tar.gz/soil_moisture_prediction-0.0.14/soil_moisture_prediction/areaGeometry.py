"""This module contains the geometry classes for the area of interest."""

import numpy as np


class RectGeom:
    """Rectangular geometry based on 4 corner points and a resolution step."""

    def __init__(self, geometry_corners):
        """Initialize the geometry based on the 4 corners and the resolution."""
        self.xi = geometry_corners[0]
        self.xf = geometry_corners[1]
        self.yi = geometry_corners[2]
        self.yf = geometry_corners[3]
        self.resolution = geometry_corners[4]

        self.grid_x, self.grid_y = np.mgrid[
            self.xi : self.xf + self.resolution : self.resolution,
            self.yi : self.yf + self.resolution : self.resolution,
        ]

        self.dim_x = self.grid_x.shape[0]
        self.dim_y = self.grid_x.shape[1]

    def find_nearest_node(self, x, y):
        """Find the nearest node in the grid to the given coordinates."""
        idx_x = np.floor((x + self.resolution / 2 - self.xi) / self.resolution).astype(
            int
        )
        idx_y = np.floor((y + self.resolution / 2 - self.yi) / self.resolution).astype(
            int
        )
        return np.column_stack((idx_x, idx_y))
