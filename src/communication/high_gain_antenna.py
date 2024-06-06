import numpy as np
from scipy.signal import butter, lfilter

class HighGainAntenna:
    def __init__(self, frequency, gain_db):
        self.frequency = frequency
        self.gain_db = gain_db
        self.antenna_array = self.create_antenna_array()

    def create_antenna_array(self):
        # Create a 2D array of antennas with optimized spacing and orientation
        num_antennas = 16
        spacing = 0.5  # wavelength
        orientation = np.pi / 4  # radians
        antenna_array = np.zeros((num_antennas, 2))
        for i in range(num_antennas):
            antenna_array[i, 0] = i * spacing * np.cos(orientation)
            antenna_array[i, 1] = i * spacing * np.sin(orientation)
        return antenna_array

    def beamform(self, signal):
        # Apply beamforming algorithm to enhance signal gain
        num_samples = len(signal)
        beamformed_signal = np.zeros(num_samples)
        for i in range(num_samples):
            beamformed_signal[i] = np.sum(signal[i] * self.antenna_array[:, 0])
        return beamformed_signal

    def filter_signal(self, signal):
        # Apply a Butterworth filter to remove noise and interference
        nyq = 0.5 * self.frequency
        cutoff = 0.1 * nyq
        order = 5
        b, a = butter(order, cutoff, btype='low')
        filtered_signal = lfilter(b, a, signal)
        return filtered_signal

    def transmit(self, data):
        # Transmit data through the high-gain antenna system
        signal = self.beamform(data)
        filtered_signal = self.filter_signal(signal)
        return filtered_signal

if __name__ == '__main__':
    antenna = HighGainAntenna(frequency=2.4e9, gain_db=30)
    data = np.random.rand(1000)  # sample data
    transmitted_signal = antenna.transmit(data)
    print("Transmitted signal:", transmitted_signal)
