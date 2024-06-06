# Sensor system for the spacecraft
import numpy as np

class SensorSystem:
    def __init__(self):
        self.temperature = 20.0
        self.humidity = 50.0

    def update_temperature(self, new_temperature):
        self.temperature = new_temperature

    def update_humidity(self, new_humidity):
        self.humidity = new_humidity

    def get_sensor_data(self):
        return np.array([self.temperature, self.humidity])
