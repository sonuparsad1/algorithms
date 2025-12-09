# Raising and Custom Exceptions

## Raising Exceptions
```python
def divide(a, b):
    if b == 0:
        raise ValueError("Divisor cannot be zero")
    return a / b

try:
    divide(10, 0)
except ValueError as e:
    print(e)
```

## Custom Exceptions
```python
class InsufficientFundsError(Exception):
    """Raised when withdrawal exceeds balance"""
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        self.balance -= amount

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(e)
```

## Re-raising Exceptions
```python
try:
    # some code
    pass
except ValueError as e:
    print("Logging error...")
    raise  # Re-raise the same exception
```

## Exception Chaining
```python
try:
    # code
    pass
except ValueError as e:
    raise TypeError("Type error occurred") from e
```
