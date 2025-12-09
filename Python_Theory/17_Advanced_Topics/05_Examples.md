# Advanced Python Examples

## Example 1: Async Web Scraper
```python
import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    urls = ['http://example.com', 'http://example.org']
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
    return results
```

## Example 2: Custom Decorator with State
```python
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Call {wrapper.calls}")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@count_calls
def greet():
    print("Hello")
```

## Example 3: Context Manager for Timing
```python
import time
from contextlib import contextmanager

@contextmanager
def timer(name):
    start = time.time()
    yield
    end = time.time()
    print(f"{name} took {end-start:.2f}s")

with timer("Operation"):
    # Do work
    time.sleep(1)
```

## Example 4: Thread Pool Executor
```python
from concurrent.futures import ThreadPoolExecutor

def process(item):
    return item * 2

items = range(10)
with ThreadPoolExecutor(max_workers=4) as executor:
    results = list(executor.map(process, items))
```

## Example 5: Custom Iterator with State
```python
class FibonacciIterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.count = 0
        self.a, self.b = 0, 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.count >= self.max_count:
            raise StopIteration
        self.count += 1
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result
```
