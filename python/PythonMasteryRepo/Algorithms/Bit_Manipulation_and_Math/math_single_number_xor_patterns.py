"""
Title: Single Number Problem (Unique in Duplicates)
Topic: Bit Manipulation and Math

Theory:
    Given array where every element appears twice except one. Find that one.
    Solution: XOR sum of all elements.
    x ^ x = 0.
    x ^ 0 = x.
    Associative.
    
    Complexity: O(N) time, O(1) space.
"""

def find_single_number(nums):
    res = 0
    for n in nums:
        res ^= n
    return res

def find_two_single_numbers(nums):
    """
    Every element appears twice except TWO numbers.
    1. XOR all -> x ^ y.
    2. Find a set bit in (x ^ y).
    3. Divide elements into two groups based on that bit.
    4. XOR each group to get x and y.
    """
    xor_sum = 0
    for n in nums:
        xor_sum ^= n
        
    # Get rightmost set bit
    right_bit = xor_sum & -xor_sum
    
    x, y = 0, 0
    for n in nums:
        if n & right_bit:
            x ^= n
        else:
            y ^= n
            
    return x, y

def run_tests():
    # 1
    arr1 = [4, 1, 2, 1, 2]
    assert find_single_number(arr1) == 4
    
    # 2
    arr2 = [4, 5, 2, 4, 1, 1] # Unique: 5, 2
    a, b = find_two_single_numbers(arr2)
    assert set([a, b]) == {5, 2}
    
    print("[PASS] Single Number Problems")

if __name__ == "__main__":
    run_tests()
