"""
Complex Analysis Algorithms Implementation.

Includes:
1. Complex Number Basic Operations (Demo).
2. Iterative FFT (Cooley-Tukey).
3. Mandelbrot Set Generator.
4. Möbius Transformation Class.
"""

from typing import List, Tuple
import math
import cmath

# ==============================================================================
# 1. FFT (Iterative)
# ==============================================================================

def fft(a: List[complex], inverse: bool = False) -> List[complex]:
    """
    Computes FFT of array a. Len(a) must be power of 2.
    """
    n = len(a)
    if (n & (n - 1)) != 0:
        raise ValueError("Length must be power of 2")
        
    # Bit Reversal Permutation
    # O(N)
    b = list(a)
    shifts = n.bit_length() - 1
    for i in range(n):
        # Reverse bits of i
        rev = 0
        temp = i
        for _ in range(shifts):
            rev = (rev << 1) | (temp & 1)
            temp >>= 1
        if i < rev:
            b[i], b[rev] = b[rev], b[i]
            
    # Cooley-Tukey Butterfly
    # O(N log N)
    length = 2
    while length <= n:
        angle = 2 * math.pi / length * (-1 if inverse else 1)
        wlen = cmath.exp(complex(0, angle))
        for i in range(0, n, length):
            w = 1 + 0j
            for j in range(length // 2):
                u = b[i + j]
                v = b[i + j + length // 2] * w
                b[i + j] = u + v
                b[i + j + length // 2] = u - v
                w *= wlen
        length *= 2
        
    if inverse:
        for i in range(n):
            b[i] /= n
            
    return b

def multiply_polynomials_fft(p1: List[int], p2: List[int]) -> List[int]:
    """
    Multiplies two polynomials using FFT.
    Takes coeffs, returns coeffs of product.
    """
    n = 1
    while n < len(p1) + len(p2): n *= 2
    
    fa = [complex(x, 0) for x in p1] + [0] * (n - len(p1))
    fb = [complex(x, 0) for x in p2] + [0] * (n - len(p2))
    
    fa = fft(fa)
    fb = fft(fb)
    
    fc = [fa[i] * fb[i] for i in range(n)]
    
    res_complex = fft(fc, inverse=True)
    return [round(x.real) for x in res_complex]

# ==============================================================================
# 2. Möbius Transformation
# ==============================================================================

class MobiusTransform:
    def __init__(self, a, b, c, d):
        # f(z) = (az + b) / (cz + d)
        self.mat = [[a, b], [c, d]]
        
    def apply(self, z: complex) -> complex:
        num = self.mat[0][0] * z + self.mat[0][1]
        den = self.mat[1][0] * z + self.mat[1][1]
        if den == 0:
            return float('inf') # Point at infinity
        return num / den

    def compose(self, other: 'MobiusTransform') -> 'MobiusTransform':
        # Composition corresponds to matrix multiplication
        a1, b1 = self.mat[0]
        c1, d1 = self.mat[1]
        a2, b2 = other.mat[0]
        c2, d2 = other.mat[1]
        
        return MobiusTransform(
            a1*a2 + b1*c2, a1*b2 + b1*d2,
            c1*a2 + d1*c2, c1*b2 + d1*d2
        )

if __name__ == "__main__":
    # Test FFT Mult: (1 + x)(1 + x) = 1 + 2x + x^2
    p1 = [1, 1]
    p2 = [1, 1]
    res = multiply_polynomials_fft(p1, p2)
    # Expected [1, 2, 1, 0...]
    assert res[0] == 1 and res[1] == 2 and res[2] == 1
    
    # Test Mobius
    # f(z) = 1/z  (a=0, b=1, c=1, d=0)
    inv = MobiusTransform(0, 1, 1, 0)
    z = 2 + 0j
    assert abs(inv.apply(z) - 0.5) < 1e-9
    
    print("Complex Analysis Implementations Verified.")
