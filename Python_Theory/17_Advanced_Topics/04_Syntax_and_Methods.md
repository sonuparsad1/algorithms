# Advanced Syntax and Patterns

## Context Manager Protocol
```python
from contextlib import contextmanager

@contextmanager
def managed_resource():
    # Setup
    resource = acquire_resource()
    try:
        yield resource
    finally:
        # Cleanup
        release_resource(resource)

with managed_resource() as r:
    use(r)
```

## Property Decorators
```python
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2
```

## Slots
```python
class Point:
    __slots__ = ['x', 'y']  # Memory optimization
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

## Abstract Base Classes
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass
```

## Dataclasses
```python
from dataclasses import dataclass, field

@dataclass
class Person:
    name: str
    age: int
    hobbies: list = field(default_factory=list)
```
