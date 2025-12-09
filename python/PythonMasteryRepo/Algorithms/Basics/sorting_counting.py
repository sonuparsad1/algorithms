"""
Title: Counting Sort
Topic: Algorithms Basics

Theory:
    Non-comparison based sort.
    Counts the number of objects having distinct key values.
    
    Complexity:
    - Time: O(n + k) where n is number of elements, k is the range of input.
    - Space: O(n + k).
    
    Constraint:
    - Efficient only when k is not significantly larger than n.
    - Typically for positive integers.
"""

def counting_sort(arr):
    if not arr:
        return arr
    
    # 1. Find range
    max_val = max(arr)
    min_val = min(arr) # Handle negatives by shifting if needed, here assuming >= 0 for simplicity or shift
    
    if min_val < 0:
        raise ValueError("This simple implementation assumes non-negative integers")

    count = [0] * (max_val + 1)
    output = [0] * len(arr)

    # 2. Store count of each character
    for num in arr:
        count[num] += 1
        
    # 3. Change count[i] so that count[i] now contains actual position
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    # 4. Build output array (Stable)
    i = len(arr) - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1
        
    return output

def run_tests():
    data = [4, 2, 2, 8, 3, 3, 1]
    res = counting_sort(data)
    assert res == [1, 2, 2, 3, 3, 4, 8]
    print("[PASS] Counting Sort")

if __name__ == "__main__":
    run_tests()
