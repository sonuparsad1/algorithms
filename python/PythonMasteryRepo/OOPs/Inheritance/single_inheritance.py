"""
Title: Single Inheritance
Topic: Inheritance

Theory:
    Single Inheritance: A Child class inherits from exactly one Parent class.
    
    Terminology:
    - Base Class / Parent Class / Super Class
    - Derived Class / Child Class / Sub Class

    Benefits: Reuse code, extend functionality.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

class Dog(Animal):
    def bark(self):
        return "Woof!"

def run_test():
    d = Dog("Buddy")
    # Method from Parent
    assert d.eat() == "Buddy is eating."
    # Method from Child
    assert d.bark() == "Woof!"
    
    print("[PASS] Single inheritance")

if __name__ == "__main__":
    run_test()
