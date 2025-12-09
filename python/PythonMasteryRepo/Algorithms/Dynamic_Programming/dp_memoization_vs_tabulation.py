"""
Title: DP Intro (Memoization vs Tabulation)
Topic: Dynamic Programming

Theory:
    DP solves problems by breaking them into overlapping subproblems.
    
    1. Memoization (Top-Down): Recursive. Caches results of function calls.
    2. Tabulation (Bottom-Up): Iterative. Fills a table (array) from base cases up.
    
    Example: Fibonacci.
"""

# 1. Memoization
memo = {}
def fib_memo(n):
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n-1) + fib_memo(n-2)
    return memo[n]

# 2. Tabulation
def fib_tab(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# 3. Space Optimized Tabulation
def fib_space_opt(n):
    if n <= 1: return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def run_tests():
    n = 10
    expected = 55
    assert fib_memo(n) == expected
    assert fib_tab(n) == expected
    assert fib_space_opt(n) == expected
    
    print("[PASS] DP Intro (Fibonacci)")

if __name__ == "__main__":
    run_tests()
