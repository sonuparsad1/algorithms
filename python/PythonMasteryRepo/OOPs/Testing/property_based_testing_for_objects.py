"""
Title: Property Based Testing
Topic: Testing

Theory:
    Instead of writing specific inputs/outputs (Example-based), 
    we define properties that should hold true for ANY valid input.
    We typically generate random data to find edge cases.
    
    Real world tool: `hypothesis` library (strongly recommended).
    Here: A manual simulation to understand the concept.
"""

import random

def add(a, b):
    return a + b

def properties_of_addition():
    """Run random inputs to verify Commutative Property."""
    for _ in range(100):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        
        # Property: a + b == b + a
        assert add(a, b) == add(b, a), f"Commutativity failed for {a}, {b}"
        
        # Property: a + 0 == a
        assert add(a, 0) == a, "Identity failed"

def run_tests():
    print("Running Property Based checks...")
    try:
        properties_of_addition()
        print("[PASS] Addition properties hold for random inputs")
    except AssertionError as e:
        print(f"[FAIL] {e}")

if __name__ == "__main__":
    run_tests()
