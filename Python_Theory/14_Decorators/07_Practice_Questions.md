# Practice Questions - Decorators

## Questions

### Q1: Debug Decorator
Create a decorator that prints function name and arguments before calling it.

### Q2: Cache Decorator
Implement a simple caching decorator.

### Q3: Timing Decorator
Create a decorator that measures execution time.

### Q4: Validation Decorator
Create a decorator that validates function arguments are positive numbers.

### Q5: Singleton Decorator
Create a decorator that makes a class a singleton.

---

## Solutions

### A1: Debug Decorator
```python
from functools import wraps

def debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a + b

add(3, 5)
```

### A2: Cache Decorator
```python
def cache(func):
    cached_results = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cached_results:
            print(f"Cache hit for {args}")
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper

@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### A3: Timing Decorator
```python
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
    return "Done"
```

### A4: Validation Decorator
```python
def validate_positive(func):
    @wraps(func)
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"All arguments must be positive numbers")
        return func(*args)
    return wrapper

@validate_positive
def multiply(a, b):
    return a * b
```

### A5: Singleton Decorator
```python
def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper

@singleton
class Database:
    def __init__(self):
        print("Creating database connection")

db1 = Database()  # Creates instance
db2 = Database()  # Returns same instance
print(db1 is db2)  # True
```
