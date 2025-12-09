# Practice Questions - Advanced Topics

## Questions

### Q1: Async HTTP Requests
Create an async function that fetches multiple URLs concurrently.

### Q2: Thread-Safe Counter
Implement a thread-safe counter class.

### Q3: Custom Context Manager
Create a context manager that logs entry and exit times.

### Q4: Type-Hinted Function
Write a function with proper type hints for a generic sorting function.

### Q5: Singleton Pattern
Implement a singleton using a metaclass.

---

## Solutions

### A1: Async HTTP Requests
```python
import asyncio

async def fetch_url(url):
    # Simulated fetch
    await asyncio.sleep(1)
    return f"Content from {url}"

async def fetch_all(urls):
    tasks = [fetch_url(url) for url in urls]
    return await asyncio.gather(*tasks)

urls = ['http://example.com', 'http://example.org']
results = asyncio.run(fetch_all(urls))
```

### A2: Thread-Safe Counter
```python
import threading

class ThreadSafeCounter:
    def __init__(self):
        self._value = 0
        self._lock = threading.Lock()
    
    def increment(self):
        with self._lock:
            self._value += 1
    
    def value(self):
        with self._lock:
            return self._value
```

### A3: Custom Context Manager
```python
import time
from contextlib import contextmanager

@contextmanager
def log_time(name):
    start = time.time()
    print(f"{name} started")
    try:
        yield
    finally:
        end = time.time()
        print(f"{name} finished in {end-start:.2f}s")

with log_time("Operation"):
    time.sleep(1)
```

### A4: Type-Hinted Function
```python
from typing import List, TypeVar, Callable

T = TypeVar('T')

def sort_by(items: List[T], key: Callable[[T], int]) -> List[T]:
    return sorted(items, key=key)

# Usage
numbers = [3, 1, 4, 1, 5]
sorted_nums = sort_by(numbers, key=lambda x: x)
```

### A5: Singleton Pattern
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    def __init__(self):
        print("Creating database connection")

db1 = Database()  # Creates instance
db2 = Database()  # Returns same instance
print(db1 is db2)  # True
```
