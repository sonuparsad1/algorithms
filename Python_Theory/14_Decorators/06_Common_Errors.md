# Common Decorator Errors

## 1. Forgetting to Return Wrapper
```python
# WRONG
def decorator(func):
    def wrapper():
        func()
    # Missing return!

# CORRECT
def decorator(func):
    def wrapper():
        func()
    return wrapper
```

## 2. Not Using *args, **kwargs
```python
# WRONG
def decorator(func):
    def wrapper():  # Can't accept arguments!
        return func()
    return wrapper

# CORRECT
def decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
```

## 3. Not Using @wraps
```python
# WRONG
def decorator(func):
    def wrapper():
        return func()
    return wrapper
# func.__name__ is now "wrapper"!

# CORRECT
from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper():
        return func()
    return wrapper
```

## 4. Decorator vs Decorator Factory Confusion
```python
# Decorator (no parameters)
@my_decorator
def func():
    pass

# Decorator factory (with parameters)
@my_decorator(param)
def func():
    pass
```
