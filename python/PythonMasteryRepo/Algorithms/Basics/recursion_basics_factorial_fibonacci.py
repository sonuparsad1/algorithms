"""
Title: Recursion Basics (Factorial, Fibonacci)
Topic: Algorithms Basics

Theory:
    Function calling itself.
    Must have a Base Case to stop.
    
    Complexity:
    - Factorial: O(n) | Stack: O(n).
    - Fibonacci (Naive): O(2^n) | Stack: O(n).
    
    Pitfall: Maximum recursion depth (default 1000 in Python).
"""

import sys

# 1. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 2. Fibonacci (Naive)
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n-1) + fib_naive(n-2)

# 3. Fibonacci (Memoized)
memo = {}
def fib_memo(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    res = fib_memo(n-1) + fib_memo(n-2)
    memo[n] = res
    return res

def run_tests():
    assert factorial(5) == 120
    assert fib_naive(6) == 8 # 0 1 1 2 3 5 8
    
    sys.setrecursionlimit(2000)
    # fib_naive(50) would hang. fib_memo is instant.
    assert fib_memo(50) == 12586269025
    
    print("[PASS] Recursion basics")

if __name__ == "__main__":
    run_tests()
