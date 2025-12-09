"""
Title: Multiple Inheritance
Topic: Inheritance

Theory:
    A class can inherit from more than one parent.
    `class Child(Parent1, Parent2):`

    Complexity matches:
    - Search order matters (Left to Right).
    - The "Diamond Problem" (ambiguity) is solved by Python's MRO.

    Pitfalls:
    - Naming collisions between parents.
    - Complex dependency graphs making code hard to trace.
"""

class Flyer:
    def fly(self):
        return "I can fly"
    
    def action(self):
        return "Flying high"

class Swimmer:
    def swim(self):
        return "I can swim"

    def action(self):
        return "Swimming deep"

class Duck(Flyer, Swimmer):
    """
    Inherits from both.
    Where 'action' is defined in both, the first one in the list wins 
    unless overridden.
    Duck(Flyer, Swimmer) -> Flyer.action wins.
    """
    pass

class Penguin(Swimmer, Flyer):
    """
    Swapped order.
    Penguin(Swimmer, Flyer) -> Swimmer.action wins.
    """
    pass

def run_tests():
    d = Duck()
    assert d.fly() == "I can fly"
    assert d.swim() == "I can swim"
    # Resolution based on order
    assert d.action() == "Flying high" 

    p = Penguin()
    assert p.action() == "Swimming deep"

    print("[PASS] Multiple Inheritance basics")

if __name__ == "__main__":
    run_tests()
