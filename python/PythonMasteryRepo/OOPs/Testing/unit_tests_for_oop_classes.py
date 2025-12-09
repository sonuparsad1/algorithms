"""
Title: Unit Testing OOP Classes
Topic: Testing

Theory:
    `unittest` is the built-in framework.
    Key concepts:
    - TestCase: A class representing a test scenario.
    - `setUp`/`tearDown`: Lifecycle methods (fixtures).
    - `assert*` methods: Validation.
"""

import unittest

class Calculator:
    def add(self, a, b):
        return a + b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Zero division")
        return a / b

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Called before EACH test method."""
        self.calc = Calculator()

    def tearDown(self):
        """Called after EACH test method."""
        pass

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 1), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        # Testing Exception
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()
