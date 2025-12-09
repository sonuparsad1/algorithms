"""
Title: Callable Objects (Functors)
Topic: Advanced OOP

Theory:
    Any object that implements `__call__` can be called like a function.
    `obj()` translates to `obj.__call__()`.
    
    Use cases:
    - Stateful functions (decorators, callbacks).
    - Caching/Memoization objects.
"""

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        """Allows instance to be called like a function."""
        return value * self.factor

class CallCounter:
    def __init__(self):
        self.count = 0
    
    def __call__(self):
        self.count += 1
        return self.count

def run_tests():
    # 1. Multiplier
    double = Multiplier(2)
    triple = Multiplier(3)
    
    assert double(10) == 20
    assert triple(10) == 30
    
    # 2. Counter (Stateful)
    c = CallCounter()
    assert c() == 1
    assert c() == 2
    assert c.count == 2
    
    print("[PASS] Callable objects verified")

if __name__ == "__main__":
    run_tests()
