# GPS system for the spacecraft
import numpy as np

class GPS:
    def __init__(self):
        self.latitude = 0.0
        self.longitude = 0.0
        self.altitude = 0.0

    def update_position(self, new_latitude, new_longitude, new_altitude):
        self.latitude = new_latitude
        self.longitude = new_longitude
        self.altitude = new_altitude

    def get_position(self):
        return np.array([self.latitude, self.longitude, self.altitude])
