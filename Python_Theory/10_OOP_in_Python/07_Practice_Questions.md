# Practice Questions - OOP

## Questions

### Q1: Create a Rectangle Class
Create a `Rectangle` class with width and height. Add methods for area and perimeter.

### Q2: Implement a Stack
Create a `Stack` class with push, pop, and is_empty methods.

### Q3: Bank Account with Inheritance
Create `SavingsAccount` and `CheckingAccount` classes inheriting from `BankAccount`.

### Q4: Implement `__str__` and `__repr__`
Create a `Book` class with proper string representations.

### Q5: Abstract Shape Class
Create an abstract `Shape` class and concrete `Circle` and `Square` classes.

---

## Solutions

### A1: Rectangle Class
```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

rect = Rectangle(5, 3)
print(rect.area())       # 15
print(rect.perimeter())  # 16
```

### A2: Stack Implementation
```python
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Pop from empty stack")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # 2
```

### A3: Bank Account Inheritance
```python
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance

class SavingsAccount(BankAccount):
    def __init__(self, balance=0, interest_rate=0.02):
        super().__init__(balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        self._balance += self._balance * self.interest_rate

class CheckingAccount(BankAccount):
    def __init__(self, balance=0, overdraft_limit=100):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if self._balance - amount >= -self.overdraft_limit:
            self._balance -= amount
            return True
        return False
```

### A4: String Representations
```python
class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"

book = Book("1984", "George Orwell", 1949)
print(str(book))   # "1984" by George Orwell
print(repr(book))  # Book('1984', 'George Orwell', 1949)
```

### A5: Abstract Shape
```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"Area: {shape.area():.2f}")
```
