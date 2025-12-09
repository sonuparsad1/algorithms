# Decorator Syntax and Methods

## Basic Syntax
```python
def decorator(func):
    def wrapper(*args, **kwargs):
        # Before
        result = func(*args, **kwargs)
        # After
        return result
    return wrapper

@decorator
def my_function():
    pass
```

## With Parameters
```python
def decorator_factory(param):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Use param
            return func(*args, **kwargs)
        return wrapper
    return decorator

@decorator_factory("value")
def my_function():
    pass
```

## Class-based Decorators
```python
class Decorator:
    def __init__(self, func):
        self.func = func
    
    def __call__(self, *args, **kwargs):
        # Decorator logic
        return self.func(*args, **kwargs)
```

## functools.wraps
```python
from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserves metadata
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```
