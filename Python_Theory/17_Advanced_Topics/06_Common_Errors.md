# Common Advanced Python Errors

## 1. Async/Await Errors
```python
# WRONG - Forgetting await
async def fetch():
    return "data"

async def main():
    result = fetch()  # Returns coroutine, not "data"!

# CORRECT
async def main():
    result = await fetch()
```

## 2. Thread Safety Issues
```python
# WRONG - Race condition
counter = 0

def increment():
    global counter
    counter += 1  # Not thread-safe!

# CORRECT
import threading

lock = threading.Lock()
counter = 0

def increment():
    global counter
    with lock:
        counter += 1
```

## 3. Type Hint Misuse
```python
# WRONG - Runtime type checking doesn't happen automatically
def greet(name: str) -> str:
    return name

greet(123)  # No error! Type hints are for static analysis

# Use mypy or runtime validation if needed
```

## 4. Metaclass Conflicts
```python
# WRONG - Multiple metaclasses
class Meta1(type):
    pass

class Meta2(type):
    pass

class MyClass(metaclass=Meta1, metaclass=Meta2):  # Error!
    pass
```

## 5. Descriptor Errors
```python
# WRONG - Forgetting __set_name__
class Descriptor:
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)  # self.name not set!

# CORRECT
class Descriptor:
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
```
