# Exotic matter detector system for the spacecraft
import numpy as np

class ExoticMatterDetector:
    def __init__(self):
        self.detector_data = []

    def scan(self):
        # Scan for exotic matter
        detector_data = np.random.rand(10)  # Simulate detector data
        self.detector_data.append(detector_data)
        return detector_data

    def analyze_data(self):
        # Analyze the detector data
        analysis_result = np.random.choice(['exotic matter detected', 'no exotic matter detected'])
        return analysis_result
