"""
Title: Chinese Remainder Theorem (CRT)
Topic: Number Theory

Theory:
    Find x such that:
    x = a1 (mod n1)
    x = a2 (mod n2)
    ...
    Assumption: n1, n2... are pairwise coprime.
    
    Formula: x = sum(ai * Ni * mi) (mod N)
    where N = prod(ni), Ni = N/ni, mi = inv(Ni, ni).
"""

def mod_inverse(a, m):
    # Minimal extended euclidean implementation
    m0, x0, x1 = m, 0, 1
    if m == 1: return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += m0
    return x1

def chinese_remainder_theorem(remainders, mods):
    # x = remainders[i] mod mods[i]
    total_product = 1
    for m in mods:
        total_product *= m
        
    result = 0
    for r, m in zip(remainders, mods):
        Ni = total_product // m
        inv = mod_inverse(Ni, m)
        result += r * Ni * inv
        
    return result % total_product

def run_tests():
    # x = 2 mod 3
    # x = 3 mod 5
    # x = 2 mod 7
    # 23 % 3 = 2. 23 % 5 = 3. 23 % 7 = 2.
    assert chinese_remainder_theorem([2, 3, 2], [3, 5, 7]) == 23
    print("[PASS] CRT")

if __name__ == "__main__":
    run_tests()
