"""
Title: Bit Tricks and Hacks
Topic: Bit Manipulation and Math

Theory:
    Useful O(1) properties.
    1. Check if Power of 2: n & (n-1) == 0 (and n > 0).
    2. Count Set Bits (Kernighan's Algo): Loop n = n & (n-1) increases count.
    3. Clear lowest set bit: n & (n-1).
    4. Get lowest set bit: n & -n.
"""

def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

def count_set_bits(n):
    count = 0
    while n > 0:
        n &= (n - 1)
        count += 1
    return count

def get_lowest_set_bit(n):
    return n & -n

def run_tests():
    # Power of 2
    assert is_power_of_two(16) is True
    assert is_power_of_two(18) is False
    assert is_power_of_two(0) is False
    
    # Count bits
    # 7 is 111 -> 3
    assert count_set_bits(7) == 3
    # 16 is 10000 -> 1
    assert count_set_bits(16) == 1
    
    # Lowest set bit
    # 12 is 1100. Lowest bit is at index 2 (value 4).
    # -12 in two's complement...
    assert get_lowest_set_bit(12) == 4
    
    print("[PASS] Bit Tricks")

if __name__ == "__main__":
    run_tests()
