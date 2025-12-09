"""
Title: Docstrings and Type Annotations
Topic: OOP Basics

Theory:
    - Docstrings: Strings used to document modules, classes, functions, and methods.
      Accessible via `__doc__` attribute.
      Common styles: Google, NumPy, Sphinx/reST.
    
    - Type Annotations (Hints): Added in Python 3.5+.
      Used by static type checkers (mypy) and IDEs.
      Stored in `__annotations__`.

    Best Practices:
    - Always document public APIs.
    - Use type hints for function arguments and return types.
"""

from typing import List, Dict, Union, Optional

# ==========================================
# 1. Annotated Class with Docstrings
# ==========================================

class Student:
    """
    Represents a student in the system.

    Attributes:
        name (str): The student's full name.
        grades (List[int]): A list of scores typicaly 0-100.
    """

    def __init__(self, name: str, grades: Optional[List[int]] = None) -> None:
        """
        Initializes the student.

        Args:
            name: The name of the student.
            grades: Optional list of initial grades.
        """
        self.name: str = name
        self.grades: List[int] = grades if grades else []

    def add_grade(self, score: int) -> None:
        """
        Adds a single grade.

        Args:
            score (int): The score to add.
            
        Raises:
            ValueError: If score is out of range.
        """
        if not (0 <= score <= 100):
            raise ValueError("Score must be between 0 and 100")
        self.grades.append(score)

    def get_average(self) -> float:
        """
        Calculates the average grade.

        Returns:
            float: The average, or 0.0 if no grades.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


# ==========================================
# 2. Accessing Metadata
# ==========================================

def inspection_demo():
    print("--- Inspecting Docstrings and Annotations ---")
    
    # 1. Docstring
    print(f"Class Doc: {Student.__doc__.strip().splitlines()[0]}")
    print(f"Method Doc: {Student.add_grade.__doc__.strip().splitlines()[0]}")

    # 2. Annotations
    print(f"Init Annotations: {Student.__init__.__annotations__}")
    print(f"Method Annotations: {Student.get_average.__annotations__}")


# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    inspection_demo()
    
    s = Student("Jane", [90, 80])
    s.add_grade(100)
    assert s.get_average() == 90.0
    
    print("[PASS] Docstrings and Annotations demo passed.")
