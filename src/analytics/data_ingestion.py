# Data Ingestion System to Collect Data from Various Spacecraft Systems

import pandas as pd
import numpy as np
from kafka import KafkaConsumer
from influxdb import InfluxDBClient

class DataIngestion:
    def __init__(self):
        self.kafka_consumer = KafkaConsumer('spacecraft_data', bootstrap_servers=['localhost:9092'])
        self.influx_client = InfluxDBClient(host='localhost', port=8086)
        self.influx_client.switch_database('spacecraft_db')

    def ingest_data(self):
        # Ingest data from Kafka topic
        for message in self.kafka_consumer:
            data = message.value.decode('utf-8')
            self.process_data(data)

    def process_data(self, data):
        # Process data and write to InfluxDB
        data_points = []
        for item in data.split(','):
            key, value = item.split(':')
            data_points.append({
                'easurement': key,
                'fields': {'value': float(value)}
            })
        self.influx_client.write_points(data_points)

    def start_ingestion(self):
        # Start data ingestion
        self.ingest_data()

# Example usage:
data_ingestion = DataIngestion()
data_ingestion.start_ingestion()
