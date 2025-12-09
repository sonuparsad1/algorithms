# Common Decorator Use Cases

## Timing Decorator
```python
import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

## Logging Decorator
```python
def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

## Caching/Memoization
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Authentication Decorator
```python
def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

@require_auth
def sensitive_operation():
    pass
```
