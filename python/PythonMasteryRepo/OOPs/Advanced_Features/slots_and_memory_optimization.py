"""
Title: Slots and Memory Optimization
Topic: Advanced OOP

Theory:
    By default, Python objects use a `__dict__` to store attributes.
    This is flexible but memory-heavy for millions of objects.
    
    `__slots__`:
    - Tells Python to use a static structure (array-like) instead of dict.
    - Prevents creation of new attributes not in slots.
    - Reduces memory footprint significantly.
"""

import sys

class RegularPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class SlottedPoint:
    __slots__ = ['x', 'y']
    def __init__(self, x, y):
        self.x = x
        self.y = y

def run_tests():
    p_reg = RegularPoint(1, 2)
    p_slot = SlottedPoint(1, 2)

    # 1. Attribute Access
    assert p_reg.x == 1
    assert p_slot.x == 1

    # 2. Constraint
    p_reg.z = 3 # Allowed
    try:
        p_slot.z = 3 # Not allowed
    except AttributeError:
        print("Caught expected error: Cannot add new attribute to slotted class")

    # 3. Memory diff (Approximation)
    # Note: sys.getsizeof doesn't recursively measure __dict__ fully without help, 
    # but the object struct itself shows difference.
    
    size_reg = sys.getsizeof(p_reg) + sys.getsizeof(p_reg.__dict__)
    size_slot = sys.getsizeof(p_slot)
    
    print(f"Regular Size (approx): {size_reg} bytes")
    print(f"Slotted Size: {size_slot} bytes")
    
    assert size_slot < size_reg
    
    print("[PASS] Slots optimization")

if __name__ == "__main__":
    run_tests()
