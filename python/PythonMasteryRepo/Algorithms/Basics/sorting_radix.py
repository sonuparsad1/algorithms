"""
Title: Radix Sort
Topic: Algorithms Basics

Theory:
    Digit by digit sorting starting from least significant digit to most significant.
    Uses Counting Sort as a subroutine.
    
    Complexity:
    - Time: O(d * (n + b)) where d is digits, n is elements, b is base (10).
    - Avoids comparison.
"""

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10 # Base 10
    
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    
    exp = 1
    while max_val // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

def run_tests():
    data = [170, 45, 75, 90, 802, 24, 2, 66]
    res = radix_sort(data.copy())
    assert res == [2, 24, 45, 66, 75, 90, 170, 802]
    print("[PASS] Radix Sort")

if __name__ == "__main__":
    run_tests()
