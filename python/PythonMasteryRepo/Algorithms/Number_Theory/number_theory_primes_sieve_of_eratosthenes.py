"""
Title: Sieve of Eratosthenes (Primes)
Topic: Number Theory

Theory:
    Generate all primes up to N efficiently.
    Iteratively mark multiples of each prime as composite.
    
    Complexity: O(N log log N).
"""

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n + 1)]
    p = 2
    while (p * p <= n):
        if primes[p] == True:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
        
    primes[0] = False
    primes[1] = False # 1 is not prime
    return [p for p in range(n + 1) if primes[p]]

def run_tests():
    p = sieve_of_eratosthenes(30)
    assert p == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    print("[PASS] Sieve of Eratosthenes")

if __name__ == "__main__":
    run_tests()
