# Radar sensor system for the spacecraft
import numpy as np

class Radar:
    def __init__(self):
        self.radar_data = []

    def scan(self):
        # Simulate radar scan
        radar_data = np.random.rand(360, 2)  # Simulate 360-degree scan with 2D points
        self.radar_data.append(radar_data)
        return radar_data

    def get_radar_data(self):
        return self.radar_data
