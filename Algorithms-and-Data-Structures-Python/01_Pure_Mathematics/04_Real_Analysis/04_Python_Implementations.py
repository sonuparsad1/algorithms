"""
Real Analysis Algorithms Implementation.

Includes:
1. Root Finding (Newton, Bisection).
2. Numerical Integration (Simpson).
3. Kahan Summation.
4. AutoDiff (Toy Implementation of Forward Mode).
"""

from typing import Callable, List, Union
import math

# ==============================================================================
# 1. Root Finding
# ==============================================================================

def bisection_method(f: Callable[[float], float], a: float, b: float, tol=1e-9) -> float:
    if f(a) * f(b) > 0:
        raise ValueError("No root bracketed")
    
    mid = 0.0
    for _ in range(100): # Hard limit prevents infinite loops
        mid = (a + b) / 2
        if (b - a) < tol:
            return mid
        if f(mid) == 0:
            return mid
        
        if f(a) * f(mid) < 0:
            b = mid
        else:
            a = mid
    return mid

def newton_method(f: Callable[[float], float], df: Callable[[float], float], x0: float, tol=1e-9) -> float:
    x = x0
    for _ in range(100):
        y = f(x)
        dy = df(x)
        if abs(y) < tol:
            return x
        if dy == 0:
            raise ValueError("Derivative zero")
        x = x - y / dy
    return x

# ==============================================================================
# 2. Numerical Integration
# ==============================================================================

def simpsons_rule(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    """
    Approximates definite integral using Simpson's 1/3 rule.
    n must be even.
    """
    if n % 2 != 0: n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    
    for i in range(1, n, 2):
        s += 4 * f(a + i * h)
    for i in range(2, n - 1, 2):
        s += 2 * f(a + i * h)
        
    return s * h / 3

# ==============================================================================
# 3. Kahan Summation
# ==============================================================================

def kahan_sum(arr: List[float]) -> float:
    sum_val = 0.0
    c = 0.0 # Compensation for lost low-order bits
    for x in arr:
        y = x - c
        t = sum_val + y
        c = (t - sum_val) - y
        sum_val = t
    return sum_val

# ==============================================================================
# 4. Toy Automatic Differentiation (Forward Mode)
# ==============================================================================

class Dual:
    """
    Represents a number a + b*epsilon where epsilon^2 = 0.
    val: value
    der: derivative component
    """
    def __init__(self, val: float, der: float = 0.0):
        self.val = val
        self.der = der
        
    def __repr__(self):
        return f"Dual(val={self.val}, der={self.der})"
    
    def __add__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        return Dual(self.val + other.val, self.der + other.der)
    
    def __mul__(self, other):
        other = other if isinstance(other, Dual) else Dual(other)
        # Product Rule: (u*v)' = u'v + uv'
        return Dual(self.val * other.val, self.der * other.val + self.val * other.der)
    
    def sin(self):
        # Chain Rule: sin(u)' = cos(u) * u'
        return Dual(math.sin(self.val), math.cos(self.val) * self.der)

def differentiate(func: Callable[[Dual], Dual], x: float) -> float:
    """
    Computes derivative of func at x using Forward Mode Basic.
    """
    d = Dual(x, 1.0) # Seed derivative 1
    res = func(d)
    return res.der

if __name__ == "__main__":
    # Test Root Finding (x^2 - 4 = 0)
    root_bis = bisection_method(lambda x: x*x - 4, 0, 5)
    assert abs(root_bis - 2.0) < 1e-6
    
    root_newt = newton_method(lambda x: x*x - 4, lambda x: 2*x, 5)
    assert abs(root_newt - 2.0) < 1e-9
    
    # Test Integration (Integral x^2 dx from 0 to 3 is x^3/3 = 9)
    integ = simpsons_rule(lambda x: x*x, 0, 3, 100)
    assert abs(integ - 9.0) < 1e-6
    
    # Test Autodiff (derivative of x^2 + 2x at x=3 is 2x+2 = 8)
    def my_func(x):
        return x*x + Dual(2)*x
    
    der_val = differentiate(my_func, 3.0)
    assert abs(der_val - 8.0) < 1e-9
    
    print("All Real Analysis Implementations Verified.")
