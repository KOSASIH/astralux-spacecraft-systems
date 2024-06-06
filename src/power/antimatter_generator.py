# Antimatter generator power system for the spacecraft
import numpy as np

class AntimatterGenerator:
    def __init__(self):
        self.power_level = 100

    def generate_power(self):
        # Generate power from antimatter
        self.power_level += 10
        return self.power_level

    def get_power_level(self):
        return self.power_level
