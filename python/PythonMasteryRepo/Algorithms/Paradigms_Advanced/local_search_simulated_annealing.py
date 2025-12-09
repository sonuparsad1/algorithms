"""
Title: Local Search (Simulated Annealing)
Topic: Paradigms

Theory:
    Heuristic optimization.
    Start with random solution. Move to neighbor.
    If neighbor better, accept.
    If neighbor worse, accept with prob exp(-delta/T).
    Cool down T.
"""

import math
import random

def objective_function(x):
    # Min at x=0
    return x**2

def simulated_annealing():
    current_x = random.uniform(-10, 10)
    current_cost = objective_function(current_x)
    
    temp = 100.0
    cooling_rate = 0.99
    
    while temp > 0.1:
        new_x = current_x + random.uniform(-1, 1)
        new_cost = objective_function(new_x)
        
        if new_cost < current_cost:
            current_x = new_x
            current_cost = new_cost
        else:
            delta = new_cost - current_cost
            prob = math.exp(-delta / temp)
            if random.random() < prob:
                current_x = new_x
                current_cost = new_cost
        
        temp *= cooling_rate
        
    return current_x

def run_tests():
    # Should be close to 0
    res = simulated_annealing()
    assert abs(res) < 2.0 # Allow some margin for heuristic
    print(f"Annealing Result: {res}")
    print("[PASS] Simulated Annealing")

if __name__ == "__main__":
    run_tests()
