"""
Title: Method Overriding
Topic: Polymorphism

Theory:
    Child class provides a specific implementation of a method that is already defined in its Parent.
    This allows polymorphism: treat Child as Parent, but get Child's behavior.

    Use `super()` to extend rather than replace fully.
"""

class PaymentProcessor:
    def process_payment(self, amount):
        return "Base payment processing"

class CreditCard(PaymentProcessor):
    def process_payment(self, amount):
        # Full Override
        return f"Charging Credit Card: {amount}"

class PayPal(PaymentProcessor):
    def process_payment(self, amount):
        # Extending Base Behavior
        base_msg = super().process_payment(amount)
        return f"PayPal Wrapper -> {base_msg}"

def run_transaction(processor: PaymentProcessor, amount):
    """Polymorphic Function"""
    return processor.process_payment(amount)

def run_tests():
    cc = CreditCard()
    pp = PayPal()
    
    # Same function call, different behavior
    assert run_transaction(cc, 100) == "Charging Credit Card: 100"
    assert "PayPal Wrapper" in run_transaction(pp, 50)
    
    print("[PASS] Method overriding")

if __name__ == "__main__":
    run_tests()
