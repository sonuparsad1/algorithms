"""
Title: Properties, Getters, and Setters
Topic: OOP Basics

Theory:
    In Python, we prefer direct attribute access (public by default). 
    However, if we need validation or computed attributes, we use the `@property` decorator.
    This creates "managed attributes".

    - @property: Defines the getter.
    - @name.setter: Defines the setter.
    - @name.deleter: Defines behavior on `del obj.name`.

    Benefit: You can start with simple attributes (`self.x`) and change to properties later 
    without breaking client code (API stability).

Pitfalls:
    - Infinite recursion: Accessing `self.x` inside the setter for `x`.
      (Must use a private backing variable like `self._x`).
"""

# ==========================================
# 1. The Pythonic Way
# ==========================================

class Circle:
    def __init__(self, radius: float):
        self._radius = radius # "Protected" variable by convention

    @property
    def radius(self):
        """The radius property (Getter)."""
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """The radius setter with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        """Computed property (Read-only)."""
        return 3.14159 * (self._radius ** 2)


# ==========================================
# 2. Pitfall: Infinite Recursion
# ==========================================

class Broken:
    @property
    def x(self):
        return self.x # RECURSION ERROR! Should be self._x

    @x.setter
    def x(self, val):
        self.x = val # RECURSION ERROR!


# ==========================================
# Tests
# ==========================================

def run_tests():
    print("--- Property Tests ---")
    c = Circle(5)
    print(f"Initial Radius: {c.radius}, Area: {c.area}")
    
    # 1. Test Setter
    c.radius = 10
    assert c._radius == 10
    print(f"New Radius: {c.radius}")

    # 2. Test Validation
    try:
        c.radius = -5
    except ValueError as e:
        print(f"Caught expected error: {e}")
    
    # 3. Test Read-only
    try:
        c.area = 50 # AttributeError, no setter defined
    except AttributeError:
        print("Caught expected AttributeError for read-only property")

if __name__ == "__main__":
    run_tests()
    print("[PASS] Property tests passed.")
