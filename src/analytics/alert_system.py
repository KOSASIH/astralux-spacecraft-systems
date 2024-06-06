# Alert System to Notify Astronauts of Critical System Failures or Anomalies

import pandas as pd
import numpy as np
from influxdb import InfluxDBClient
from sklearn.ensemble import IsolationForest

class AlertSystem:
    def __init__(self):
        self.influx_client = InfluxDBClient(host='localhost', port=8086)
        self.influx_client.switch_database('spacecraft_db')
        self.model = IsolationForest(contamination=0.1)

    def fetch_data(self, measurement):
        # Fetch data from InfluxDB
        query = f'SELECT * FROM {measurement}'
        result = self.influx_client.query(query)
        data = pd.DataFrame(result.get_points(measurement=measurement))
        return data

    def detect_anomalies(self, data):
        # Detect anomalies using Isolation Forest
        predictions = self.model.fit_predict(data)
        anomalies = data[predictions == -1]
        return anomalies

    def send_alert(self, anomalies):
        # Send alert to astronauts
        print('Alert: Critical system failure or anomaly detected!')
        print(anomalies)

    def start_alert_system(self, measurement):
        # Start alert system
        while True:
            data = self.fetch_data(measurement)
            anomalies = self.detect_anomalies(data)
            if not anomalies.empty:
                self.send_alert(anomalies)

# Example usage:
alert_system = AlertSystem()
alert_system.start_alert_system('temperature')
