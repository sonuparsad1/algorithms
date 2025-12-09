# Object-Oriented Programming (OOP) in Python

## Definition

**OOP** is a programming paradigm based on the concept of "objects" which contain data (attributes) and code (methods).

## Core Concepts

### 1. Class
A blueprint for creating objects.

### 2. Object
An instance of a class.

### 3. The Four Pillars of OOP

#### Encapsulation
Bundling data and methods that operate on that data within a single unit (class).

#### Inheritance
Creating new classes from existing ones, inheriting attributes and methods.

#### Polymorphism
The ability to use a common interface for multiple forms (data types).

#### Abstraction
Hiding complex implementation details and showing only necessary features.

## Basic Class Syntax
```python
class Dog:
    # Class attribute
    species = "Canis familiaris"
    
    # Constructor
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

print(dog1.bark())  # "Buddy says Woof!"
```
