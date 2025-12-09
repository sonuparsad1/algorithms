"""
Title: Static Methods vs Class Methods
Topic: OOP Basics

Theory:
    - Instance Methods: Receive `self` (the instance). Can access instance and class state.
    - Class Methods (`@classmethod`): Receive `cls` (the class). Can access class state, but not instance state.
      Often used for "Factory Methods" (alternative constructors).
    - Static Methods (`@staticmethod`): Receive neither `self` nor `cls`.
      Behave like regular functions but belong to the class namespace for logical grouping.

    When to use:
    - @classmethod: When you need access to class variables or want to return an instance of `cls`.
    - @staticmethod: When the method doesn't touch the object or class internals (utility functions).

Pitfalls:
    - Using a static method when a class method was needed (e.g., hardcoding class name in static method vs using `cls`).
"""

import datetime

# ==========================================
# 1. Implementation
# ==========================================

class DateHelper:
    # Class variable
    date_format = "%Y-%m-%d"

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def display(self):
        """Instance method"""
        return f"{self.year}/{self.month}/{self.day}"

    @classmethod
    def from_string(cls, date_str: str):
        """
        Class Method used as a Factory.
        It uses 'cls' to instantiate the object, supporting inheritance.
        """
        y, m, d = map(int, date_str.split("-"))
        # Returns an instance of 'cls' (DateHelper or subclass)
        return cls(y, m, d)

    @classmethod
    def set_format(cls, new_format):
        """Modifies class state."""
        cls.date_format = new_format

    @staticmethod
    def is_valid_date(year, month, day):
        """
        Static Method. 
        Does not need self or cls. Just logic related to dates.
        """
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        return True

# ==========================================
# 2. Inheritance Behavior
# ==========================================

class DetailedDate(DateHelper):
    def display(self):
        return f"Detailed: {super().display()}"

def run_demo():
    print("--- Static vs Class Methods ---")
    
    # 1. Using Factory (Class Method)
    d1 = DateHelper.from_string("2023-10-25")
    print(f"Factory created: {d1.display()}")
    assert d1.year == 2023

    # 2. Inheritance check
    # calling from_string on subclass should return instance of SUBCLASS
    d2 = DetailedDate.from_string("2024-01-01")
    print(f"Subclass factory: {d2.display()}") 
    assert isinstance(d2, DetailedDate) # Crucial check!

    # 3. Static Method usage
    valid = DateHelper.is_valid_date(2023, 13, 1) # False
    print(f"Is 2023-13-1 valid? {valid}")
    assert valid is False


# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    run_demo()
    print("[PASS] Static/Class method tests passed.")
