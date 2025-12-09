# OOP Examples

## Example 1: Library Management System
```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
    
    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False
    
    def return_book(self):
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

# Usage
lib = Library()
book1 = Book("Python 101", "John Doe", "123")
lib.add_book(book1)
book1.borrow()
```

## Example 2: Employee Management
```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def give_raise(self, amount):
        self.salary += amount

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department
        self.team = []
    
    def add_team_member(self, employee):
        self.team.append(employee)

manager = Manager("Alice", 100000, "Engineering")
emp1 = Employee("Bob", 70000)
manager.add_team_member(emp1)
```

## Example 3: Game Character System
```python
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
    
    def is_alive(self):
        return self.health > 0

class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=150)
        self.armor = 20
    
    def take_damage(self, damage):
        reduced_damage = max(0, damage - self.armor)
        super().take_damage(reduced_damage)

warrior = Warrior("Conan")
warrior.take_damage(30)  # Takes 10 damage (30 - 20 armor)
```
