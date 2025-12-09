# Decorator Examples

## Example 1: Retry Decorator
```python
import time
from functools import wraps

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_api_call():
    # May fail randomly
    pass
```

## Example 2: Validation Decorator
```python
def validate_positive(func):
    @wraps(func)
    def wrapper(x):
        if x <= 0:
            raise ValueError("Must be positive")
        return func(x)
    return wrapper

@validate_positive
def square_root(x):
    return x ** 0.5
```

## Example 3: Rate Limiting
```python
import time

def rate_limit(calls_per_second):
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(2)  # Max 2 calls per second
def api_call():
    pass
```
