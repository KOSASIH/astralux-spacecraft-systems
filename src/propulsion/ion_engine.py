# Ion engine system for the spacecraft
import numpy as np

class IonEngine:
    def __init__(self):
        self.thrust_level = 0

    def set_thrust_level(self, thrust_level):
        self.thrust_level = thrust_level

    def get_thrust(self):
        return self.thrust_level * 100  # Simulate thrust in Newtons

    def optimize_thrust(self, mission_requirements):
        # Optimize thrust level based on mission requirements
        if mission_requirements['mission_type'] == 'interplanetary':
            self.thrust_level = 0.5
        elif mission_requirements['mission_type'] == 'orbital':
            self.thrust_level = 0.2
        return self.thrust_level
