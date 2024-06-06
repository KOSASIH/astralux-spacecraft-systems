# Stellar navigation system for the spacecraft
import numpy as np
from scipy.optimize import least_squares

class StellarNavigation:
    def __init__(self):
        self.star_catalog = []

    def add_star(self, star_id, ra, dec):
        self.star_catalog.append((star_id, ra, dec))

    def determine_position(self, observed_stars):
        def residual(params):
            # Calculate the residual between the observed and predicted star positions
            predicted_positions = []
            for star in observed_stars:
                predicted_positions.append(predict_position(params, star))
            return np.array(predicted_positions) - np.array(observed_stars)

        params_initial = np.array([1, 2, 3, 4, 5, 6])  # Initial guess for the position parameters
        result = least_squares(residual, params_initial)
        return result.x
