# Battery management system for the spacecraft
import numpy as np

class BatteryManagement:
    def __init__(self):
        self.battery_capacity = 100.0  # Ah
        self.battery_state_of_charge = 50.0  # %

    def update_battery_state(self, delta_capacity):
        self.battery_state_of_charge += delta_capacity / self.battery_capacity * 100

    def get_battery_state(self):
        return self.battery_state_of_charge
