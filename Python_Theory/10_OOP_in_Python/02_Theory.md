# OOP Theory - Inheritance and Polymorphism

## Inheritance

### Single Inheritance
```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

class Cat(Animal):
    def speak(self):
        return f"{self.name} meows"

dog = Dog("Buddy")
print(dog.speak())  # "Buddy barks"
```

### Multiple Inheritance
```python
class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"

class Duck(Flyer, Swimmer):
    pass

duck = Duck()
print(duck.fly())   # "Flying"
print(duck.swim())  # "Swimming"
```

### Method Resolution Order (MRO)
```python
class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B, C):
    pass

d = D()
d.method()  # "B" (follows MRO: D -> B -> C -> A)
print(D.mro())  # Shows resolution order
```

## Polymorphism

### Method Overriding
```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Polymorphism in action
shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())
```

## `super()` Function
```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call parent constructor
        self.age = age
```
