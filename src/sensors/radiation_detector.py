# Radiation detector system for the spacecraft
import numpy as np

class RadiationDetector:
    def __init__(self):
        self.radiation_levels = []

    def measure_radiation(self):
        # Simulate measuring radiation levels
        radiation_level = np.random.normal(0, 1)
        self.radiation_levels.append(radiation_level)
        return radiation_level

    def get_radiation_levels(self):
        return self.radiation_levels
