import unittest
from src.propulsion.main import PropulsionSystem

class TestPropulsionSystem(unittest.TestCase):
    def test_calculate_thrust(self):
        propulsion_system = PropulsionSystem(
            thrust_vector=np.array([1, 0, 0]),
            mass_flow_rate=10,
            specific_impulse=300
        )

        thrust = propulsion_system.calculate_thrust()
        self.assertAlmostEqual(thrust, 3000, places=2)

    def test_optimize_thrust(self):
        propulsion_system = PropulsionSystem(
            thrust_vector=np.array([1, 0, 0]),
            mass_flow_rate=10,
            specific_impulse=300
        )

        optimized_thrust_vector = propulsion_system.optimize_thrust()
        self.assertAlmostEqual(optimized_thrust_vector[0], 1.2, places=2)

if __name__ == "__main__":
    unittest.main()
