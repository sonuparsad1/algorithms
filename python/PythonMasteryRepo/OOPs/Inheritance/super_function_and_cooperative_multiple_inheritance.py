"""
Title: Super() and Cooperative Multiple Inheritance
Topic: Inheritance

Theory:
    `super()` returns a proxy object that delegates method calls to a parent/sibling class 
    **based on the MRO**, not just the immediate parent.
    
    "Cooperative Inheritance":
    - Classes are designed to work together in a hierarchy.
    - Each class calls `super().method()`, passing arguments along.
    - This ensures every class in the diamond gets called exactly once (if structured correctly).

    Pitfall:
    - Mixing classes that user `super()` with classes that don't (breaking the chain).
    - Arguments mismatch in the chain (`*args, **kwargs` is often needed).
"""

class BaseModule:
    def __init__(self):
        print("BaseModule Init")

class LoggerMixin(BaseModule):
    def __init__(self):
        print("LoggerMixin Init Start")
        super().__init__() # Calls next in MRO
        print("LoggerMixin Init End")

class DatabaseMixin(BaseModule):
    def __init__(self):
        print("DatabaseMixin Init Start")
        super().__init__() # Calls next in MRO
        print("DatabaseMixin Init End")

class App(LoggerMixin, DatabaseMixin):
    """
    MRO: App -> LoggerMixin -> DatabaseMixin -> BaseModule -> object
    """
    def __init__(self):
        print("App Init Start")
        super().__init__()
        print("App Init End")

def run_demo():
    print("--- Cooperative Init Chain ---")
    # Expected Output flow:
    # App Start -> Logger Start -> Database Start -> Base -> Database End -> Logger End -> App End
    app = App()
    
    # Verify MRO
    mro_names = [c.__name__ for c in App.mro()]
    assert mro_names == ['App', 'LoggerMixin', 'DatabaseMixin', 'BaseModule', 'object']
    print("\n[PASS] Cooperative inheritance demonstrated")

if __name__ == "__main__":
    run_demo()
