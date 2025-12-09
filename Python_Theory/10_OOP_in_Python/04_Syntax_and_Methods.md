# Class Methods, Static Methods, and Abstract Classes

## Class Methods
```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)

d = Date.from_string("2024-12-09")
```

## Static Methods
```python
class Math:
    @staticmethod
    def add(x, y):
        return x + y

result = Math.add(5, 3)  # No instance needed
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

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

# shape = Shape()  # TypeError: Can't instantiate abstract class
circle = Circle(5)  # OK
```

## Dataclasses (Python 3.7+)
```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5

p = Point(3, 4)
print(p)  # Point(x=3, y=4)
```
