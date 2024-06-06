# Dataset for Training the AGI System

import pandas as pd
import numpy as np

class AGITrainingData:
    def __init__(self):
        self.data = pd.DataFrame({
            'situation': [],
            'recommendations': []
        })

    def add_data(self, situation, recommendations):
        self.data = self.data.append({'situation': situation, 'recommendations': recommendations}, ignore_index=True)

    def get_data(self):
        return self.data

    def save_data(self, filename):
        self.data.to_csv(filename, index=False)

    def load_data(self, filename):
        self.data = pd.read_csv(filename)

# Example usage:
agi_training_data = AGITrainingData()
agi_training_data.add_data([1, 2, 3], [4, 5, 6])
agi_training_data.add_data([7, 8, 9], [10, 11, 12])
agi_training_data.save_data('agi_training_data.csv')
