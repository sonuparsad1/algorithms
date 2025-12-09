# Async Programming and Concurrency

## Asyncio Basics
```python
import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)
    print("World")

# Run
asyncio.run(say_hello())
```

## Concurrent Execution
```python
async def task1():
    await asyncio.sleep(1)
    return "Task 1"

async def task2():
    await asyncio.sleep(1)
    return "Task 2"

async def main():
    # Run concurrently
    results = await asyncio.gather(task1(), task2())
    print(results)

asyncio.run(main())
```

## Threading
```python
import threading
import time

def worker(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} done")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(f"Thread-{i}",))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

## Multiprocessing
```python
from multiprocessing import Process, Pool

def square(n):
    return n * n

# Process
p = Process(target=square, args=(5,))
p.start()
p.join()

# Pool
with Pool(4) as pool:
    results = pool.map(square, range(10))
```

## Thread Safety
```python
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1
```
