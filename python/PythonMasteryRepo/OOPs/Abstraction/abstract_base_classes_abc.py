"""
Title: Abstract Base Classes (ABCs)
Topic: Abstraction

Theory:
    ABCs define a blueprint for a class. They generally cannot be instantiated.
    They force subclasses to implement specific methods using `@abstractmethod`.

    Module: `abc`
    Class: `ABC`
"""

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    
    @abstractmethod
    def authorize(self, amount):
        pass

    @abstractmethod
    def charge(self, amount):
        pass
    
    # Concrete method in ABC is allowed
    def common_log(self, msg):
        return f"LOG: {msg}"

class Stripe(PaymentGateway):
    def authorize(self, amount):
        return f"Stripe authorized {amount}"

    def charge(self, amount):
        return f"Stripe charged {amount}"

class BadGateway(PaymentGateway):
    # Missing 'charge' implementation
    def authorize(self, amount):
        pass

def run_tests():
    s = Stripe()
    assert s.authorize(100) == "Stripe authorized 100"
    assert s.common_log("Test") == "LOG: Test"

    try:
        b = BadGateway()
    except TypeError as e:
        print(f"Caught expected error: {e}")
        # "Can't instantiate abstract class BadGateway with abstract method charge"

    print("[PASS] ABC implementation")

if __name__ == "__main__":
    run_tests()
