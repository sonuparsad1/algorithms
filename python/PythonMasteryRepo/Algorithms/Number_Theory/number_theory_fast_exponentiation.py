"""
Title: Fast Exponentiation (Modular Exponentiation)
Topic: Number Theory

Theory:
    Compute (base^exp) % mod efficiently.
    O(log exp).
    Using binary representation of exp.
"""

def power(base, exp, mod):
    res = 1
    base = base % mod
    while exp > 0:
        if exp % 2 == 1: # Odd
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

def run_tests():
    # 2^10 = 1024. 1024 % 1000 = 24.
    assert power(2, 10, 1000) == 24
    print("[PASS] Fast Exponentiation")

if __name__ == "__main__":
    run_tests()
