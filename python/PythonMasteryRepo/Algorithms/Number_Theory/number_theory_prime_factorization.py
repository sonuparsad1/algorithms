"""
Title: Prime Factorization
Topic: Number Theory

Theory:
    Express a number as a product of prime numbers.
    Trial division method: Check divisibility by d from 2 up to sqrt(n).
"""

def prime_factorization(n):
    factors = []
    # 1. 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # 2. Odds starting 3
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 2
        
    # 3. Remaining prime > 2
    if n > 2:
        factors.append(n)
        
    return factors

def run_tests():
    assert prime_factorization(315) == [3, 3, 5, 7] # 9*5*7 = 45*7 = 315
    print("[PASS] Prime Factorization")

if __name__ == "__main__":
    run_tests()
