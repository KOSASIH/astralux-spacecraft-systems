# Gravity sensor system for the spacecraft
import numpy as np

class GravitySensor:
    def __init__(self):
        self.gravity_readings = []

    def measure_gravity(self):
        # Simulate measuring gravity
        gravity_reading = np.random.normal(9.8, 0.1)
        self.gravity_readings.append(gravity_reading)
        return gravity_reading

    def get_gravity_readings(self):
        return self.gravity_readings
