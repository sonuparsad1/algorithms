"""
Title: Operator Overloading (Magic Methods)
Topic: Polymorphism

Theory:
    Python allows changing the meaning of operators (+, -, *, ==) for custom classes.
    Double underscore methods (`__dunder__`) handle this.

    Common ones:
    - `__add__(self, other)` -> `+`
    - `__sub__(self, other)` -> `-`
    - `__eq__(self, other)`  -> `==`
    - `__lt__(self, other)`  -> `<`
    - `__str__` vs `__repr__`
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        raise TypeError("Can only add Vector to Vector")

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False

    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

def run_tests():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2 # Calls __add__
    
    assert v3.x == 4
    assert v3.y == 6
    
    assert v1 != v2
    assert Vector(1, 2) == v1
    
    print(f"String Rep: {v1}")
    print("[PASS] Operator overloading")

if __name__ == "__main__":
    run_tests()
