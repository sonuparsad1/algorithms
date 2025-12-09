# Common OOP Errors

## 1. Forgetting `self`
```python
# WRONG
class Dog:
    def bark():  # Missing self
        print("Woof")

# CORRECT
class Dog:
    def bark(self):
        print("Woof")
```

## 2. Not Calling Parent Constructor
```python
# WRONG
class Child(Parent):
    def __init__(self, name, age):
        self.age = age  # Parent's __init__ not called!

# CORRECT
class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
```

## 3. Mutable Class Attributes
```python
# WRONG
class MyClass:
    items = []  # Shared across all instances!
    
    def add_item(self, item):
        self.items.append(item)

# CORRECT
class MyClass:
    def __init__(self):
        self.items = []  # Instance attribute
```

## 4. Circular Imports
```python
# file_a.py
from file_b import ClassB
class ClassA:
    pass

# file_b.py
from file_a import ClassA  # Circular!
class ClassB:
    pass

# SOLUTION: Use local imports or restructure
```

## 5. Modifying Immutable Objects
```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, dx, dy):
        # If Point should be immutable, return new instance
        return Point(self.x + dx, self.y + dy)
```
