# Decorators in Python

## Definition

A **decorator** is a function that takes another function and extends its behavior without explicitly modifying it. Decorators use the `@` syntax.

## Basic Decorator
```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before function call
# Hello!
# After function call
```

## How Decorators Work
```python
# These are equivalent:
@my_decorator
def func():
    pass

# Same as:
def func():
    pass
func = my_decorator(func)
```

## Decorators with Arguments
```python
def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Arguments: {args}, {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")
```

## Preserving Metadata
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves func.__name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
