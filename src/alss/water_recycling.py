# Water Recycling System to Conserve Water Resources

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from influxdb import InfluxDBClient

class WaterRecycling:
    def __init__(self):
        self.influx_client = InfluxDBClient(host='localhost', port=8086)
        self.influx_client.switch_database('alss_db')
        self.model = RandomForestClassifier(n_estimators=100)

    def fetch_data(self):
        # Fetch water quality data from InfluxDB
        query = 'SELECT * FROM water_quality'
        result = self.influx_client.query(query)
        data = pd.DataFrame(result.get_points(measurement='water_quality'))
        return data

    def train_model(self, data):
        # Train machine learning model to classify water quality
        X = data.drop(['quality'], axis=1)
        y = data['quality']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict_water_quality(self, data):
        # Predict water quality using trained model
        predictions = self.model.predict(data)
        return predictions

    def recycle_water(self, predictions):
        # Recycle water based on predicted quality
        if predictions == 1:  # Good quality
            print('Water recycled for drinking and hygiene')
        elif predictions == 2:  # Fair quality
            print('Water recycled for irrigation and cleaning')
        else:  # Poor quality
            print('Water discarded and replaced with fresh supply')

    def start_water_recycling(self):
        # Start water recycling system
        while True:
            data = self.fetch_data()
            self.train_model(data)
            predictions = self.predict_water_quality(data)
            self.recycle_water(predictions)

# Example usage:
water_recycling = WaterRecycling()
water_recycling.start_water_recycling()
