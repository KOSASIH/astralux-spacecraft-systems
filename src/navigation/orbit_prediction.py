# Orbit prediction system for the spacecraft
import numpy as np
from scipy.optimize import least_squares

class OrbitPrediction:
    def __init__(self):
        self.orbit_data = []

    def add_orbit_data(self, position, velocity):
        self.orbit_data.append((position, velocity))

    def predict_orbit(self):
        def residual(params):
            # Calculate the residual between the predicted and actual orbit positions
            predicted_positions = []
            for i in range(len(self.orbit_data)):
                predicted_positions.append(predict_position(params, self.orbit_data[i][1]))
            return np.array(predicted_positions) - np.array([data[0] for data in self.orbit_data])

        params_initial = np.array([1, 2, 3, 4, 5, 6])  # Initial guess for the orbit parameters
        result = least_squares(residual, params_initial)
        return result.x
