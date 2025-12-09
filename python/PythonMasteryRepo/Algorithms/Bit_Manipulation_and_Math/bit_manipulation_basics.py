"""
Title: Bit Manipulation Basics
Topic: Bit Manipulation and Math

Theory:
    Operations on bits directly.
    & (AND): Both 1 -> 1
    | (OR): Either 1 -> 1
    ^ (XOR): Different -> 1
    ~ (NOT): Invert bits (Two's complement in Python: ~x = -x-1)
    << (Left Shift): Multiply by 2^k
    >> (Right Shift): Divide by 2^k
"""

def basic_ops(a, b):
    print(f"a={a} ({bin(a)}), b={b} ({bin(b)})")
    print(f"a & b: {a & b} ({bin(a & b)})")
    print(f"a | b: {a | b} ({bin(a | b)})")
    print(f"a ^ b: {a ^ b} ({bin(a ^ b)})")
    print(f"~a: {~a} ({bin(~a)})")
    print(f"a << 1: {a << 1} ({bin(a << 1)})")
    print(f"a >> 1: {a >> 1} ({bin(a >> 1)})")

def swap_xor(a, b):
    # Swap without temp variable
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def run_tests():
    a, b = 10, 20
    basic_ops(a, b)
    
    # Operations check
    # 10: 1010
    # 20: 10100
    # 10&20: 00000 -> 0
    assert (10 & 20) == 0
    # 10|20: 11110 -> 30
    assert (10 | 20) == 30
    
    # Swap
    na, nb = swap_xor(10, 20)
    assert na == 20
    assert nb == 10
    
    print("[PASS] Bit Manipulation Basics")

if __name__ == "__main__":
    run_tests()
