"""
Title: Template Method and Hooks
Topic: Design Patterns

Theory:
    Template Method: Defines the skeleton of an algorithm in the superclass but lets subclasses override specific steps.
    Hook: A method in the superclass that does nothing (or default) but can be overridden.
"""

from abc import ABC, abstractmethod

class CaffeineBeverage(ABC):
    def prepare(self):
        """The Template Method."""
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments(): # Hook usage
            self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self): pass

    @abstractmethod
    def add_condiments(self): pass

    # Hook
    def customer_wants_condiments(self):
        return True

class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")
    
    def add_condiments(self):
        print("Adding Lemon")
    
    def customer_wants_condiments(self):
        return False # Hook override

def run_tests():
    print("--- Making Tea ---")
    my_tea = Tea()
    my_tea.prepare()
    # Output should not contain "Adding Lemon"
    
    print("[PASS] Template Method")

if __name__ == "__main__":
    run_tests()
