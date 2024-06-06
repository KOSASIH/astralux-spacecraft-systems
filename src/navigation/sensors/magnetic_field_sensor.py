# Magnetic field sensor system for the spacecraft
import numpy as np

class MagneticFieldSensor:
    def __init__(self):
        self.magnetic_field_readings = []

    def measure_magnetic_field(self):
        # Simulate measuring magnetic field
        magnetic_field_reading = np.random.normal(0, 1)
        self.magnetic_field_readings.append(magnetic_field_reading)
        return magnetic_field_reading

    def get_magnetic_field_readings(self):
        return self.magnetic_field_readings
