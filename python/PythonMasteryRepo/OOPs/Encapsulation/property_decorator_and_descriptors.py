"""
Title: Property Decorator and Descriptors
Topic: Encapsulation

Theory:
    We've seen basic `@property`. This file looks closer at how it encapsulates logic.
    Also introduces the concept of Descriptors: the mechanism behind properties.

    - A Descriptor is any object that defines `__get__`, `__set__`, or `__delete__`.
    - Properties are implementing the descriptor protocol.

    Use Case: 
    - Validation logic reuse. If multiple attributes need similar validation (e.g., "must be positive integer"),
      writing a custom descriptor is better than multiple properties.

"""

# ==========================================
# 1. Reuse logic with Descriptors
# ==========================================

class PositiveInteger:
    """A Descriptor for enforcing positive integers."""
    
    def __init__(self, default=0):
        self.default = default
        self.data = {} # Simulating storage (In real descriptors, use instance.__dict__)

    def __set_name__(self, owner, name):
        # Called when the descriptor is instantiated in a class
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, self.default)

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name} must be an integer")
        if value < 0:
            raise ValueError(f"{self.name} must be positive")
        instance.__dict__[self.name] = value


class Rectangle:
    # Using the descriptor
    width = PositiveInteger()
    height = PositiveInteger()

    def __init__(self, w, h):
        self.width = w
        self.height = h

    @property # Standard property for computed value
    def area(self):
        return self.width * self.height


# ==========================================
# 2. Standard Property (Encapsulation logic)
# ==========================================

class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is impossible")
        self._temperature = value

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32


# ==========================================
# Tests
# ==========================================

def run_tests():
    print("--- Descriptor & Property Tests ---")

    # 1. Descriptor
    r = Rectangle(10, 20)
    assert r.area == 200
    
    try:
        r.width = -5
    except ValueError as e:
        print(f"Caught descriptor error: {e}")

    # 2. Property
    c = Celsius(25)
    assert c.to_fahrenheit() == 77.0
    
    try:
        c.temperature = -300
    except ValueError as e:
        print(f"Caught property error: {e}")

if __name__ == "__main__":
    run_tests()
    print("[PASS] All tests passed.")
