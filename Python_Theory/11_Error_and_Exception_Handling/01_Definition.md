# Error and Exception Handling

## Definition

**Exceptions** are events that disrupt the normal flow of a program. **Exception handling** allows you to gracefully handle errors instead of crashing.

## Exception Hierarchy
```
BaseException
├── SystemExit
├── KeyboardInterrupt
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   └── OverflowError
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    ├── TypeError
    ├── ValueError
    ├── NameError
    └── ... (many more)
```

## Basic Try-Except
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Multiple Exceptions
```python
try:
    value = int(input("Enter number: "))
    result = 10 / value
except ValueError:
    print("Invalid input!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

## Catching Multiple Exceptions
```python
try:
    # code
    pass
except (ValueError, TypeError) as e:
    print(f"Error: {e}")
```

## The `else` Clause
```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Result: {result}")  # Runs if no exception
```

## The `finally` Clause
```python
try:
    file = open("data.txt")
    # process file
except FileNotFoundError:
    print("File not found")
finally:
    # Always executes
    print("Cleanup code")
```
