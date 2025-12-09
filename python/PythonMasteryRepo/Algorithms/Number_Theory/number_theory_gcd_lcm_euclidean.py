"""
Title: GCD and LCM (Euclidean Algorithm)
Topic: Number Theory

Theory:
    GCD (Greatest Common Divisor): Largest number dividing both a and b.
    LCM (Least Common Multiple): Smallest number divisible by both.
    
    Formula: a * b = GCD(a, b) * LCM(a, b).
    
    Euclidean Algorithm:
    gcd(a, b) = gcd(b, a % b).
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0: return 0
    return abs(a * b) // gcd(a, b)

def gcd_extended(a, b):
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that ax + by = g = gcd(a, b).
    """
    if a == 0:
        return b, 0, 1
    
    g, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y

def run_tests():
    assert gcd(48, 18) == 6
    assert lcm(4, 5) == 20
    
    g, x, y = gcd_extended(35, 15)
    # 35x + 15y = 5.
    # 35(1) + 15(-2) = 35 - 30 = 5.
    assert g == 5
    assert 35*x + 15*y == 5
    
    print("[PASS] GCD and LCM")

if __name__ == "__main__":
    run_tests()
