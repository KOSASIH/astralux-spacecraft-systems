# LiDAR sensor system for the spacecraft
import numpy as np

class LiDAR:
    def __init__(self):
        self.scan_data = []

    def scan(self):
        # Simulate LiDAR scan
        scan_data = np.random.rand(360, 2)  # Simulate 360-degree scan with 2D points
        self.scan_data.append(scan_data)
        return scan_data

    def get_scan_data(self):
        return self.scan_data
