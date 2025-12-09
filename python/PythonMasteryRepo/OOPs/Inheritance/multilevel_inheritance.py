"""
Title: Multilevel Inheritance
Topic: Inheritance

Theory:
    A class inherits from a child class, forming a chain.
    GrandParent -> Parent -> Child.

    MRO (Method Resolution Order) is linear here.
"""

class Organism:
    def live(self):
        return "I am alive"

class Animal(Organism):
    def eat(self):
        return "I eat food"

class Dog(Animal):
    def bark(self):
        return "Woof"

def run_test():
    d = Dog()
    assert d.live() == "I am alive" # From GrandParent
    assert d.eat() == "I eat food"  # From Parent
    assert d.bark() == "Woof"       # From Child
    
    # Check inheritance chain
    assert isinstance(d, Dog)
    assert isinstance(d, Animal)
    assert isinstance(d, Organism)
    
    print("[PASS] Multilevel inheritance")

if __name__ == "__main__":
    run_test()
