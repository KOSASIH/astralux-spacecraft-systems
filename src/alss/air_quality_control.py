# Air Quality Control System to Maintain a Healthy Atmosphere

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from influxdb import InfluxDBClient

class AirQualityControl:
    def __init__(self):
        self.influx_client = InfluxDBClient(host='localhost', port=8086)
        self.influx_client.switch_database('alss_db')
        self.model = RandomForestRegressor(n_estimators=100)

    def fetch_data(self):
        # Fetch air quality data from InfluxDB
        query = 'SELECT * FROM air_quality'
        result = self.influx_client.query(query)
        data = pd.DataFrame(result.get_points(measurement='air_quality'))
        return data

    def train_model(self, data):
        # Train machine learning model to predict air quality
        X = data.drop(['CO2', 'O2', 'temperature', 'humidity'], axis=1)
        y = data['CO2']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)

    def predict_air_quality(self, data):
        # Predict air quality using trained model
        predictions = self.model.predict(data)
        return predictions

    def control_air_quality(self, predictions):
        # Control air quality by adjusting ventilation, filtration, and temperature
        if predictions > 1000:  # ppm CO2
            print('Ventilation system activated to reduce CO2 levels')
        elif predictions < 500:  # ppm CO2
            print('Filtration system activated to increase O2 levels')
        else:
            print('Air quality within safe limits')

    def start_air_quality_control(self):
        # Start air quality control system
        while True:
            data = self.fetch_data()
            self.train_model(data)
            predictions = self.predict_air_quality(data)
            self.control_air_quality(predictions)

# Example usage:
air_quality_control = AirQualityControl()
air_quality_control.start_air_quality_control()
