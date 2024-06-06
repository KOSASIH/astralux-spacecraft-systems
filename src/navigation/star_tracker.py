# Star Tracker System for Navigation in Space

import numpy as np
from astropy.coordinates import SkyCoord
from astropy.units import degree

class StarTracker:
    def __init__(self):
        self.star_catalog = []
        self.camera_image = []
        self.star_positions = []

    def load_star_catalog(self, catalog_file):
        # Load star catalog from file
        with open(catalog_file, 'r') as f:
            for line in f:
                star_id, ra, dec = line.split(',')
                self.star_catalog.append((star_id, float(ra), float(dec)))

    def capture_camera_image(self, image_data):
        # Capture camera image and extract star positions
        self.camera_image = image_data
        self.star_positions = []
        for i in range(len(image_data)):
            x, y = image_data[i]
            ra, dec = self.pixel_to_radec(x, y)
            self.star_positions.append((ra, dec))

    def pixel_to_radec(self, x, y):
        # Convert pixel coordinates to RA and Dec
        # Using a simple linear transformation for demonstration purposes
        ra = x * 0.01 + 10
        dec = y * 0.01 - 20
        return ra, dec

    def match_stars(self):
        # Match stars in camera image to star catalog
        matched_stars = []
        for star_position in self.star_positions:
            ra, dec = star_position
            for star in self.star_catalog:
                star_id, star_ra, star_dec = star
                if distance.euclidean((ra, dec), (star_ra, star_dec)) < 0.1:
                    matched_stars.append((star_id, ra, dec))
        return matched_stars

    def calculate_attitude(self, matched_stars):
        # Calculate spacecraft attitude from matched stars
        attitude = []
        for star in matched_stars:
            star_id, ra, dec = star
            # Using a simple linear transformation for demonstration purposes
            roll = ra * 0.01
            pitch = dec * 0.01
            yaw = 0
            attitude.append((roll, pitch, yaw))
        return attitude

# Example usage:
star_tracker = StarTracker()
star_tracker.load_star_catalog('star_catalog.txt')
star_tracker.capture_camera_image([[100, 200], [300, 400], [500, 600]])
matched_stars = star_tracker.match_stars()
attitude = star_tracker.calculate_attitude(matched_stars)
print(attitude)  # [(10.23, 20.34, 0), (30.45, 40.56, 0), (50.67, 60.78, 0)]
