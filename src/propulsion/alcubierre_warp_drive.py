# Alcubierre warp drive propulsion system for the spacecraft
import numpy as np

class AlcubierreWarpDrive:
    def __init__(self):
        self.warp_factor = 1.0
        self.exotic_matter_level = 100

    def engage_warp(self, warp_factor):
        # Engage the Alcubierre warp drive
        self.warp_factor = warp_factor
        self.exotic_matter_level -= 10
        return self.warp_factor

    def get_warp_factor(self):
        return self.warp_factor

    def get_exotic_matter_level(self):
        return self.exotic_matter_level
