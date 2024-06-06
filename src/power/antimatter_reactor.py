# Antimatter reactor power system for the spacecraft
import numpy as np

class AntimatterReactor:
    def __init__(self):
        self.power_level = 100

    def generate_power(self):
        # Simulate generating power from the antimatter reactor
        self.power_level += 10
        return self.power_level

    def get_power_level(self):
        return self.power_level
