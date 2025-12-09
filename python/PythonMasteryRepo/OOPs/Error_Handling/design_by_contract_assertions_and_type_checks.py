"""
Title: Design by Contract (Assertions and Type Checks)
Topic: Error Handling

Theory:
    DbC defines Preconditions (Args valid), Postconditions (Return valid), and Invariants (State valid).
    
    Python tools:
    - `assert`: Optimized out with `-O`. Good for internal sanity checks.
    - Exceptions: For runtime input validation (Public API).
"""

def divide(a, b):
    # Precondition (Internal)
    assert isinstance(a, (int, float)), "a must be number"
    assert isinstance(b, (int, float)), "b must be number"
    assert b != 0, "b cannot be zero"
    
    result = a / b
    
    # Postcondition
    assert result * b == a, "Math broken" 
    return result

class Account:
    def __init__(self, balance):
        self._balance = balance
        self._invariant()

    def _invariant(self):
        assert self._balance >= 0, "Balance cannot be negative"

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        self._invariant()

def run_tests():
    assert divide(10, 2) == 5.0
    
    try:
        divide(10, 0)
    except AssertionError as e:
        print(f"Caught assertion: {e}")

    acc = Account(100)
    acc.withdraw(50)
    
    print("[PASS] DbC assertions")

if __name__ == "__main__":
    run_tests()
