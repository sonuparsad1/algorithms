"""
Title: Modular Arithmetic
Topic: Number Theory

Theory:
    (a + b) % m = ((a % m) + (b % m)) % m
    (a * b) % m = ((a % m) * (b % m)) % m
    
    Modular Inverse:
    (a / b) % m -> a * inv(b) % m.
    inv(b) exists only if gcd(b, m) = 1.
    If m is prime, inv(b) = b^(m-2) % m (Fermat's Little Theorem).
"""

def mod_add(a, b, m):
    return (a + b) % m

def mod_mul(a, b, m):
    return (a * b) % m

def mod_inverse(a, m):
    # Setup for extended GCD
    def egcd(a, b):
        if a == 0: return b, 0, 1
        g, x1, y1 = egcd(b % a, a)
        x = y1 - (b // a) * x1
        y = x1
        return g, x, y

    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError("Inverse doesn't exist")
    return (x % m + m) % m

def run_tests():
    # 3 * x = 1 (mod 11). x = 4. (3*4 = 12 = 1 mod 11)
    assert mod_inverse(3, 11) == 4
    
    print("[PASS] Modular Arithmetic")

if __name__ == "__main__":
    run_tests()
