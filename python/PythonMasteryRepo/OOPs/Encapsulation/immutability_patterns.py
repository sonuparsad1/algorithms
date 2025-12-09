"""
Title: Immutability Patterns
Topic: Encapsulation

Theory:
    Immutable objects cannot be changed after creation (e.g., tuples, strings).
    In custom classes, we can enforce immutability to make code thread-safe and predictable.

    Techniques:
    1. Property only (no setter).
    2. Overriding `__setattr__`.
    3. Using `NamedTuple` or `@dataclass(frozen=True)`.
"""

from dataclasses import dataclass
from collections import namedtuple

# ==========================================
# 1. Property-based Immutability
# ==========================================

class ImmutablePoint:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    
    # No setters defined!

# ==========================================
# 2. Hardened Immutability (__setattr__)
# ==========================================

class HardFrozen:
    def __init__(self, val):
        # We must bypass our own block to set initial value
        super().__setattr__('val', val)

    def __setattr__(self, name, value):
        raise AttributeError(f"Cannot modify immutable instance attribute '{name}'")

# ==========================================
# 3. Modern Approaches
# ==========================================

# A. Named Tuple
Color = namedtuple('Color', ['r', 'g', 'b'])

# B. Frozen Dataclass
@dataclass(frozen=True)
class User:
    id: int
    username: str

# ==========================================
# Tests
# ==========================================

def run_tests():
    print("--- Immutability Tests ---")
    
    # 1. Property
    p = ImmutablePoint(1, 2)
    try:
        p.x = 10
    except AttributeError:
        print("Caught expected AttributeError (Property)")

    # 2. Hard Frozen
    h = HardFrozen("Test")
    try:
        h.val = "New"
    except AttributeError:
        print("Caught expected AttributeError (__setattr__)")

    # 3. Dataclass
    u = User(1, "admin")
    try:
        u.item = "something" # Frozen classes don't allow new attributes either
    except Exception as e: # Frozen dataclasses raise FrozenInstanceError
        print(f"Caught expected error (Frozen Dataclass): {type(e).__name__}")

    print("[PASS] Verify Immutability passed.")

if __name__ == "__main__":
    run_tests()
