"""
Title: Constructors and __init__
Topic: OOP Basics

Theory:
    In Python, `__init__` is the initializer method, not the constructor.
    The actual constructor is `__new__` (rarely used, mostly for metaclasses or immutable types).
    
    `__init__` is called immediately after the object is created to initialize its state.

    Key Concepts:
    - Default arguments: Allow flexibility in object creation.
    - Type hints: Highly recommended for `__init__` arguments.
    - `__new__` vs `__init__`: `__new__` creates the instance, `__init__` initializes it.

Pitfalls:
    - Returning a value from `__init__`: It must return `None`.
    - Using mutable default arguments in `__init__` (e.g., `def __init__(self, items=[])`).
"""

from typing import Optional, List

# ==========================================
# 1. Standard Init with Validation
# ==========================================

class Person:
    def __init__(self, name: str, age: int):
        # Validation in init
        if age < 0:
            raise ValueError("Age cannot be negative")
        
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Person(name='{self.name}', age={self.age})"


# ==========================================
# 2. Init with Default Arguments (Correct Way)
# ==========================================

class ShoppingCart:
    def __init__(self, items: Optional[List[str]] = None):
        """
        CORRECT: Use None as default for mutable types, then create new list.
        """
        if items is None:
            self.items = []
        else:
            self.items = items

    def add(self, item: str):
        self.items.append(item)


# ==========================================
# 3. The `__new__` Method (Advanced)
# ==========================================

class Singleton:
    """A Class that allows only one instance (Singleton Pattern via __new__)."""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            print("Creating the object...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self, value):
        self.value = value


# ==========================================
# 4. Pitfalls
# ==========================================

class BadInit:
    def __init__(self, data=[]): # BAD!
        self.data = data

def demonstrate_pitfall():
    print("\n--- Init Pitfall ---")
    b1 = BadInit()
    b1.data.append("A")
    
    b2 = BadInit()
    print(f"b2 data (should be empty): {b2.data}") 
    # b2.data is ['A'] because the default list is created once at definition!
    assert "A" in b2.data


# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    # 1. Validation Test
    try:
        p = Person("John", -1)
    except ValueError as e:
        print(f"[PASS] Caught expected error: {e}")

    # 2. Correct Defaults
    c1 = ShoppingCart()
    c1.add("Apple")
    c2 = ShoppingCart()
    assert "Apple" not in c2.items
    print("[PASS] Mutable default argument handled correctly")

    # 3. Singleton
    s1 = Singleton(10)
    s2 = Singleton(20)
    assert s1 is s2
    print(f"[PASS] Singleton identity check: s1 is s2")

    # 4. Pitfall
    demonstrate_pitfall()
