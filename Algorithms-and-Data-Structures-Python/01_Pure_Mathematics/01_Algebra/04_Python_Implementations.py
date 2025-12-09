"""
Algebraic Algorithms Implementation.

Includes:
1. GCD and Extended GCD (Iterative & Recursive)
2. Modular Inverse and Exponentiation
3. Chinese Remainder Theorem Class
4. Matrix Multiplication and Exponentiation (for Linear Recurrences)
5. discrete_log (Baby-step Giant-step)
"""

from typing import Tuple, List, Optional
import math

# ==============================================================================
# 1. Basic Number Theory Helpers
# ==============================================================================

def gcd(a: int, b: int) -> int:
    """
    Compute Euclidean GCD of a and b.
    Complexity: O(log(min(a, b)))
    """
    while b:
        a, b = b, a % b
    return a

def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (g, x, y) such that ax + by = g = gcd(a, b).
    Complexity: O(log(min(a, b)))
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = extended_gcd(b % a, a)
        return g, x - (b // a) * y, y

def mod_inverse(a: int, m: int) -> int:
    """
    Compute modular multiplicative inverse of a under modulo m.
    Raises ValueError if inverse does not exist (gcd(a, m) != 1).
    """
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError(f"Modular inverse does not exist for {a} modulo {m}")
    return (x % m + m) % m

def binary_exponentiation(base: int, exp: int, mod: int) -> int:
    """
    Compute (base^exp) % mod using Square-and-Multiply.
    Complexity: O(log exp)
    """
    res = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % mod
        base = (base * base) % mod
        exp //= 2
    return res

# ==============================================================================
# 2. Chinese Remainder Theorem
# ==============================================================================

class ChineseRemainderSolver:
    """
    Solves system of congruences:
    x = a1 (mod n1)
    x = a2 (mod n2)
    ...
    Assumes n_i correspond to pairwise coprime moduli.
    """
    
    @staticmethod
    def solve(remainders: List[int], moduli: List[int]) -> int:
        prod = 1
        for n in moduli:
            prod *= n
            
        result = 0
        for a_i, n_i in zip(remainders, moduli):
            p = prod // n_i
            result += a_i * mod_inverse(p, n_i) * p
        return result % prod

# ==============================================================================
# 3. Matrix Exponentiation (for Recurrences)
# ==============================================================================

class MatrixMod:
    """
    Matrix operations under modulo m.
    """
    def __init__(self, mat: List[List[int]], mod: int):
        self.mat = mat
        self.mod = mod
        self.rows = len(mat)
        self.cols = len(mat[0])

    @staticmethod
    def identity(n: int, mod: int) -> 'MatrixMod':
        mat = [[0] * n for _ in range(n)]
        for i in range(n):
            mat[i][i] = 1
        return MatrixMod(mat, mod)

    def __mul__(self, other: 'MatrixMod') -> 'MatrixMod':
        if self.cols != other.rows:
            raise ValueError("Matrix dimensions mismatch")
        
        res = [[0] * other.cols for _ in range(self.rows)]
        for i in range(self.rows):
            for k in range(self.cols):
                if self.mat[i][k] == 0: continue
                for j in range(other.cols):
                    res[i][j] = (res[i][j] + self.mat[i][k] * other.mat[k][j]) % self.mod
        return MatrixMod(res, self.mod)

    def pow(self, exp: int) -> 'MatrixMod':
        res = MatrixMod.identity(self.rows, self.mod)
        base = self
        while exp > 0:
            if exp % 2 == 1:
                res = res * base
            base = base * base
            exp //= 2
        return res

# ==============================================================================
# 4. Discrete Logarithm (Baby-step Giant-step)
# ==============================================================================

def discrete_log(a: int, b: int, m: int) -> Optional[int]:
    """
    Solves a^x = b (mod m) for x.
    Time Complexity: O(sqrt(m))
    Space Complexity: O(sqrt(m))
    """
    a %= m
    b %= m
    n = int(math.sqrt(m)) + 1
    
    # Baby steps: store a^j (mod m) for 0 <= j < n
    value_map = {}
    curr = 1
    for j in range(n):
        value_map[curr] = j
        curr = (curr * a) % m
        
    # Giant steps: check b * (a^(-n))^i for matches
    # a^x = b => a^(i*n + j) = b => a^j = b * (a^-n)^i
    
    try:
        factor = mod_inverse(binary_exponentiation(a, n, m), m)
    except ValueError:
        return None # Inverse doesn't exist implies 'a' not coprime to m
        
    cur_val = b
    for i in range(n + 1):
        if cur_val in value_map:
            res = i * n + value_map[cur_val]
            return res
        cur_val = (cur_val * factor) % m
        
    return None

if __name__ == "__main__":
    # Test GCD
    assert gcd(48, 18) == 6
    g, x, y = extended_gcd(35, 15)
    assert 35*x + 15*y == g
    
    # Test Matrix Exp (Fibonacci)
    # [ F_n+1 ] = [ 1 1 ] [ F_n   ]
    # [ F_n   ]   [ 1 0 ] [ F_n-1 ]
    mod = 10**9 + 7
    fib_matrix = MatrixMod([[1, 1], [1, 0]], mod)
    # F_10 = 55. Matrix^9 * [1, 0] gives F_10 at index [0][0] roughly
    res_mat = fib_matrix.pow(9)
    # Start vector [F_1, F_0] = [1, 0]
    # Result [F_10, F_9]
    f_10 = (res_mat.mat[0][0] * 1 + res_mat.mat[0][1] * 0) % mod
    assert f_10 == 55
    
    # Test Discrete Log: 3^x = 13 (mod 17) -> 3^4 = 81 = 13 mod 17
    assert discrete_log(3, 13, 17) == 4
    
    print("All Algebra implementations passed.")
