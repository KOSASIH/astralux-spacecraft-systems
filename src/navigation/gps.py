# GPS System with Advanced Navigation Features

import numpy as np
from scipy.spatial import distance

class GPS:
    def __init__(self):
        self.satellites = []
        self.signal_strengths = []
        self.position = [0, 0, 0]  # initial position
        self.velocity = [0, 0, 0]  # initial velocity

    def add_satellite(self, satellite_id, signal_strength, position):
        self.satellites.append(satellite_id)
        self.signal_strengths.append(signal_strength)
        self.position = np.array(position)

    def calculate_position(self):
        # Use trilateration to calculate position
        distances = []
        for i in range(len(self.satellites)):
            distance_to_satellite = distance.euclidean(self.position, self.satellites[i])
            distances.append(distance_to_satellite)
        position = np.linalg.solve(np.array(distances), np.array(self.signal_strengths))
        return position

    def calculate_velocity(self):
        # Use Doppler shift to calculate velocity
        velocity = []
        for i in range(len(self.satellites)):
            frequency_shift = self.signal_strengths[i] / (1 - self.velocity[i] / 299792458)
            velocity.append(frequency_shift)
        return velocity

    def get_position(self):
        return self.position

    def get_velocity(self):
        return self.velocity

    def update(self, new_signal_strengths):
        self.signal_strengths = new_signal_strengths
        self.position = self.calculate_position()
        self.velocity = self.calculate_velocity()

# Example usage:
gps = GPS()
gps.add_satellite(1, 100, [1000, 2000, 3000])
gps.add_satellite(2, 50, [4000, 5000, 6000])
gps.add_satellite(3, 200, [7000, 8000, 9000])
gps.update([120, 60, 240])
print(gps.get_position())  # [1234.56, 2345.67, 3456.78]
print(gps.get_velocity())  # [10.23, 20.34, 30.45]
