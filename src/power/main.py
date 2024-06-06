# Power system for the spacecraft
import numpy as np

class PowerSystem:
    def __init__(self):
        self.battery_level = 100.0

    def update_battery_level(self, delta_level):
        self.battery_level += delta_level

    def get_battery_level(self):
        return self.battery_level
