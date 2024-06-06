# Integration tests for the navigation system
import unittest
from src.navigation.main import NavigationSystem

class TestNavigationSystem(unittest.TestCase):
    def test_update_position(self):
        nav_system = NavigationSystem()
        nav_system.update_position(10)
        self.assertEqual(nav_system.position, np.array([0, 0, 100]))

    def test_set_course(self):
        nav_system = NavigationSystem()
        nav_system.set_course([1, 2, 3])
        self.assertEqual(nav_system.velocity, np.array([1, 2, 3]))
