# Type Hints and Metaprogramming

## Type Hints
```python
from typing import List, Dict, Optional, Union, Callable, TypeVar

# Basic types
def greet(name: str, age: int) -> str:
    return f"{name} is {age}"

# Collections
def process(items: List[int]) -> Dict[str, int]:
    return {"sum": sum(items)}

# Optional
def find(name: str) -> Optional[str]:
    return name if name else None

# Union
def parse(value: Union[int, str]) -> int:
    return int(value)

# Callable
def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

# Generic
T = TypeVar('T')
def first(items: List[T]) -> T:
    return items[0]
```

## Metaclasses
```python
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    pass

db1 = Database()
db2 = Database()
print(db1 is db2)  # True
```

## Descriptors
```python
class Validator:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        if not self.min_value <= value <= self.max_value:
            raise ValueError(f"Value must be between {self.min_value} and {self.max_value}")
        setattr(obj, self.name, value)

class Person:
    age = Validator(0, 150)
    
    def __init__(self, age):
        self.age = age
```
