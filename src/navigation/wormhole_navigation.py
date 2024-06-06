# Wormhole navigation system for the spacecraft
import numpy as np

class WormholeNavigation:
    def __init__(self):
        self.wormhole_stability = 0.5

    def navigate_wormhole(self, destination):
        # Navigate through the wormhole to the destination
        navigation_data = np.random.rand(3)  # Simulate navigation data
        self.wormhole_stability += 0.1
        return navigation_data

    def get_wormhole_stability(self):
        return self.wormhole_stability
