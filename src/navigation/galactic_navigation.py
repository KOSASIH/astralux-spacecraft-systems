# Galactic navigation system for the spacecraft
import numpy as np
from astropy.coordinates import SkyCoord

class GalacticNavigation:
    def __init__(self):
        self.galactic_map = []

    def add_waypoint(self, waypoint_data):
        self.galactic_map.append(waypoint_data)

    def navigate(self, current_position):
        # Calculate the navigation data based on the galactic map and current position
        navigation_data = []
        for waypoint in self.galactic_map:
            distance = np.linalg.norm(np.array(waypoint['position']) - np.array(current_position))
            navigation_data.append((waypoint['name'], distance))
        return navigation_data
