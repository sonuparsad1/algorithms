"""
Title: Classes and Objects in Python
Topic: OOP Basics

Theory:
    A Class is a blueprint for creating objects (a particular data structure), providing initial values 
    for state (member variables or attributes), and implementations of behavior (member functions or methods).
    An Object is an instance of a Class.

    Python is completely object-oriented: everything is an object (integers, strings, functions, classes themselves).

    Key Concepts:
    - `class` keyword: Defines a new class.
    - Attributes: Data stored inside an object.
    - Methods: Functions defined inside a class that operate on its objects.
    - `self`: Reference to the current instance of the class (explicitly passed as first argument).

Complexity:
    - Object creation: O(1) typically.
    - Attribute access: O(1) (average case via dictionary lookup).

Pitfalls:
    - Forgetting `self` in method definitions (leads to "takes 0 positional arguments but 1 was given").
    - Modifying class attributes expecting them to be instance attributes.
"""

# ==========================================
# 1. Basic Class Definition
# ==========================================

class Dog:
    """A simple class representing a Dog."""

    # Class Attribute (Shared by all instances)
    species = "Canis familiaris"

    def __init__(self, name: str, age: int):
        """
        The Initializer (Constructor). 
        Called when a new instance is created.
        """
        # Instance Attributes (Unique to each instance)
        self.name = name
        self.age = age

    def description(self):
        """Instance method: operates on 'self'."""
        return f"{self.name} is {self.age} years old."

    def speak(self, sound: str):
        return f"{self.name} says {sound}"


# ==========================================
# 2. Creating and Using Objects
# ==========================================

def demonstration():
    print("--- Creating Objects ---")
    dog1 = Dog("Buddy", 9)
    dog2 = Dog("Miles", 4)

    print(f"Dog 1: {dog1.description()}")
    print(f"Dog 2: {dog2.description()}")

    # Accessing Class Attributes
    print(f"Both are: {Dog.species}")
    print(f"Dog 1 species: {dog1.species}")


# ==========================================
# 3. Pitfalls & Variations
# ==========================================

class EmptyClass:
    """Python requires 'pass' for empty blocks."""
    pass

def pitfalls_example():
    """
    Common Pitfall: Mutable Class Attributes
    """
    class DangerousDog:
        tricks = [] # Mistake: List is shared by all dogs!
        
        def __init__(self, name):
            self.name = name
        
        def add_trick(self, trick):
            self.tricks.append(trick)

    d1 = DangerousDog("Fido")
    d2 = DangerousDog("Buddy")
    
    d1.add_trick("roll over")
    # d2 will also have "roll over" now!
    assert "roll over" in d2.tricks
    print(f"\n[Pitfall Demo] d2 has tricks: {d2.tricks} (Shared State Issue)")


# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    print("Running demonstration...")
    demonstration()
    pitfalls_example()

    # Simple Asserts
    my_dog = Dog("Rex", 5)
    assert my_dog.name == "Rex"
    assert my_dog.age == 5
    assert my_dog.speak("Woof") == "Rex says Woof"
    assert isinstance(my_dog, Dog)
    
    print("\n[PASS] All basic class tests passed.")
