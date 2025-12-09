"""
Title: Catalan Numbers
Topic: Bit Manipulation and Math

Theory:
    Sequence of natural numbers with many applications.
    C_n = (2n)! / ((n+1)! * n!)
    
    Applications:
    1. Number of correct bracket sequences of length 2n.
    2. Number of BSTs with n nodes.
    3. Number of triangulations of (n+2)-gon.
"""

import math

def catalan_formula(n):
    # C_n = (1 / n+1) * nCr(2n, n)
    # nCr = (2n)! / (n! * (2n - n)!) = (2n)! / (n! * n!)
    numerator = math.factorial(2 * n)
    denominator = math.factorial(n + 1) * math.factorial(n)
    return numerator // denominator

def catalan_dp(n):
    # C_0 = 1
    # C_n+1 = sum(C_i * C_{n-i}) for i=0 to n
    if n == 0: return 1
    catalan = [0] * (n + 1)
    catalan[0] = 1
    
    for i in range(1, n + 1):
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
            
    return catalan[n]

def run_tests():
    # C_3 = 5. ((), ()(), (())(), ... 5 BSTs with 3 nodes)
    # C_4 = 14
    assert catalan_formula(3) == 5
    assert catalan_dp(3) == 5
    
    assert catalan_formula(4) == 14
    
    print("[PASS] Catalan Numbers")

if __name__ == "__main__":
    run_tests()
