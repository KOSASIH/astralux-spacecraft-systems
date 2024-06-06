# Warp drive propulsion system for the spacecraft
import numpy as np

class WarpDrive:
    def __init__(self):
        self.warp_factor = 1.0

    def engage_warp(self, warp_factor):
        # Engage the warp drive
        self.warp_factor = warp_factor
        return self.warp_factor

    def get_warp_factor(self):
        return self.warp_factor
