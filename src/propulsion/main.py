import numpy as np
from scipy.optimize import minimize

class PropulsionSystem:
    def __init__(self, thrust_vector, mass_flow_rate, specific_impulse):
        self.thrust_vector = thrust_vector
        self.mass_flow_rate = mass_flow_rate
        self.specific_impulse = specific_impulse

    def calculate_thrust(self):
        return self.thrust_vector * self.mass_flow_rate * self.specific_impulse

    def optimize_thrust(self):
        def objective_function(thrust_vector):
            return -self.calculate_thrust(thrust_vector)

        result = minimize(objective_function, self.thrust_vector, method="SLSQP")
        return result.x

if __name__ == "__main__":
    propulsion_system = PropulsionSystem(
        thrust_vector=np.array([1, 0, 0]),
        mass_flow_rate=10,
        specific_impulse=300
    )

    optimized_thrust_vector = propulsion_system.optimize_thrust()
    print("Optimized thrust vector:", optimized_thrust_vector)
