"""
Title: Decorators (Function and Class)
Topic: Advanced OOP

Theory:
    Decorators wrap functions or classes to modify behavior.
    Syntax: `@decorator`
    
    Types:
    1. Function Decorators: `def wrapper(func):`
    2. Class Decorators: `def wrapper(cls):`
    
    Preserving metadata (`functools.wraps`) is essential.
"""

from functools import wraps

# ==========================================
# 1. Function Decorator
# ==========================================

def log_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@log_call
def adder(a, b):
    """Adds two numbers."""
    return a + b


# ==========================================
# 2. Class Decorator
# ==========================================

def singleton(cls):
    instances = {}
    @wraps(cls)
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Loading Database...")

def run_tests():
    # 1. Function
    assert adder(2, 3) == 5
    assert adder.__name__ == "adder" # preserved by wraps

    # 2. Class singleton wrapper
    d1 = Database()
    d2 = Database()
    assert d1 is d2
    
    print("[PASS] Decorators")

if __name__ == "__main__":
    run_tests()
