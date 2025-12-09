"""
Title: Private and Protected Members
Topic: Encapsulation

Theory:
    Python does not have strict private/protected access modifiers like Java or C++.
    It uses naming conventions:
    
    1. Public (`self.name`): Accessible from anywhere.
    2. Protected (`self._name`): Strong convention. Should only be accessed within the class 
       and subclasses. No enforcement by language.
    3. Private (`self.__name`): Naming convention that triggers "Name Mangling". 
       Makes it harder (but not impossible) to access from outside.

    Pitfalls:
    - Relying on `__private` for security. It's just for avoiding namespace collisions in subclasses.
"""

# ==========================================
# 1. Implementation
# ==========================================

class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner       # Public
        self._balance = balance  # Protected (Convention)
        self.__pin = 1234        # Private (Name Mangled)

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}")

    def _internal_audit(self):
        """Protected method: internal use only."""
        return f"Audit: {self._balance}"

    def verify_pin(self, pin: int) -> bool:
        return self.__pin == pin


class SavingsAccount(BankAccount):
    def add_interest(self):
        # We can access _balance (Protected)
        interest = self._balance * 0.05
        self._balance += interest
        
    def try_access_pin(self):
        try:
            return self.__pin # Error! __pin is mangled in Parent
        except AttributeError:
            return "Cannot access __pin directly"


# ==========================================
# 2. Access outside class
# ==========================================

def demonstration():
    print("--- Access Modifiers ---")
    acc = BankAccount("Alice", 1000)

    # Public
    print(f"Owner: {acc.owner}")

    # Protected - Mutable from outside (Not recommended but possible)
    print(f"Balance (Protected): {acc._balance}") 
    acc._balance = 5000 
    assert acc._balance == 5000

    # Private - AttributeError
    try:
        print(acc.__pin)
    except AttributeError:
        print("Caught expected error: 'BankAccount' object has no attribute '__pin'")
    
    # Accessing Mangled Name (The bypass)
    # _ClassName__AttributeName
    print(f"Mangled Pin access: {acc._BankAccount__pin}")
    assert acc._BankAccount__pin == 1234


# ==========================================
# Tests
# ==========================================

if __name__ == "__main__":
    demonstration()

    s = SavingsAccount("Bob", 500)
    s.add_interest()
    assert s._balance == 525.0
    
    assert s.try_access_pin() == "Cannot access __pin directly"
    
    print("\n[PASS] Private/Protected tests passed.")
