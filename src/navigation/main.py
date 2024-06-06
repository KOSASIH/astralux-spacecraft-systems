# Navigation system for the spacecraft
import numpy as np

class NavigationSystem:
    def __init__(self):
        self.position = np.array([0, 0, 0])
        self.velocity = np.array([0, 0, 0])

    def update_position(self, delta_time):
        self.position += self.velocity * delta_time

    def set_course(self, new_course):
        self.velocity = np.array([new_course[0], new_course[1], new_course[2]])
