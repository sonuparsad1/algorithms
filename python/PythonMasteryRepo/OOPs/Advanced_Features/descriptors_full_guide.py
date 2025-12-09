"""
Title: Descriptors (Full Guide)
Topic: Advanced OOP

Theory:
    Descriptors are objects that define `__get__`, `__set__`, or `__delete__`.
    They are the mechanism behind properties, methods, static methods, and class methods.

    - Data Descriptor: Defines `__set__` or `__delete__`.
    - Non-Data Descriptor: Defines only `__get__` (e.g., methods).

    Crucial: Descriptors are assigned to Class attributes, not instance attributes during init.
"""

import weakref

class Typed:
    """A descriptor that enforces type checking."""
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f"Expected {self.expected_type}")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Person:
    # Descriptors must be class attributes
    name = Typed("name", str)
    age = Typed("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age

def run_tests():
    p = Person("Bob", 30)
    assert p.name == "Bob"
    assert p.age == 30
    
    try:
        p.age = "Old"
    except TypeError as e:
        print(f"Caught expected type error: {e}")

    try:
        p.name = 123
    except TypeError:
        print("Caught name error")
        
    print("[PASS] Descriptor full guide")

if __name__ == "__main__":
    run_tests()
