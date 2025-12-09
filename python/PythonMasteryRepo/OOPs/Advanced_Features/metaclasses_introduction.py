"""
Title: Metaclasses Introduction
Topic: Advanced OOP

Theory:
    In Python, Classes are objects too.
    - An Object is an instance of a Class.
    - A Class is an instance of a Metaclass.
    
    Default Metaclass: `type`.
    
    When you define `class Foo:` Python effectively does:
    `Foo = type('Foo', (bases,), dict(attributes))`
    
    To define a custom metaclass, inherit from `type` and use `metaclass=Meta` in class def.
"""

def simple_metaclass_demo():
    print("--- Dynamic Class Creation with 'type' ---")
    
    # Creating a class dynamically
    # class DynamicUser:
    #     role = "User"
    #     def __init__(self, name): self.name = name
    
    def init(self, name):
        self.name = name

    DynamicUser = type(
        'DynamicUser',          # Name
        (),                     # Bases
        {'role': 'User', '__init__': init}  # Dict
    )
    
    u = DynamicUser("Alice")
    assert u.name == "Alice"
    assert u.role == "User"
    assert type(DynamicUser) is type


class MetaVerbose(type):
    """A metaclass that logs class creation."""
    
    def __new__(mcs, name, bases, dct):
        print(f"Allocating memory for class: {name}")
        return super().__new__(mcs, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f"Initializing class: {name}")
        super().__init__(name, bases, dct)

class SpiedClass(metaclass=MetaVerbose):
    pass

def run_tests():
    simple_metaclass_demo()
    
    print("Checking SpiedClass...")
    # The print statements happened at DEFINITION time (above), not instantiation time.
    s = SpiedClass()
    assert isinstance(s, SpiedClass)
    
    print("[PASS] Metaclass intro")

if __name__ == "__main__":
    run_tests()
