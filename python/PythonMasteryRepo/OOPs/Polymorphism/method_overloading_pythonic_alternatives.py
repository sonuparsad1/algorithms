"""
Title: Method Overloading (And Pythonic Alternatives)
Topic: Polymorphism

Theory:
    Traditional Overloading (Same method name, different signatures) is NOT supported in Python.
    Defining the method twice simply overwrites the first one.

    Pythonic Alternatives:
    1. Default Arguments (`def foo(x, y=None)`).
    2. Variable Arguments (`*args`, `**kwargs`).
    3. `functools.singledispatch` (for type-based overloading).
"""

from functools import singledispatch
from typing import Union

# ==========================================
# 1. Using Default Arguments (Most Common)
# ==========================================

class MathOps:
    def add(self, a, b, c=0):
        """Simulates add(a,b) and add(a,b,c)"""
        return a + b + c


# ==========================================
# 2. Using *args (Variable Length)
# ==========================================

class Logger:
    def log(self, message, *args):
        """Simulates multiple log signatures"""
        full_msg = message
        for arg in args:
            full_msg += f" {arg}"
        return full_msg


# ==========================================
# 3. Using Single Dispatch (Type-based)
# ==========================================

@singledispatch
def process(data):
    """Base generic function"""
    raise ValueError("Unknown type")

@process.register(int)
def _(data):
    return f"Processing integer: {data}"

@process.register(list)
def _(data):
    return f"Processing list of length {len(data)}"

# ==========================================
# Tests
# ==========================================

def run_tests():
    # 1. Defaults
    m = MathOps()
    assert m.add(1, 2) == 3
    assert m.add(1, 2, 3) == 6
    
    # 2. Args
    l = Logger()
    assert l.log("Error", 404, "Not Found") == "Error 404 Not Found"

    # 3. Single Dispatch
    assert process(10) == "Processing integer: 10"
    assert process([1,2,3]) == "Processing list of length 3"
    
    print("[PASS] Overloading patterns working")

if __name__ == "__main__":
    run_tests()
