"""
Title: Divide and Conquer Strategies
Topic: Paradigms

Theory:
    Break problem into subproblems, solve them, and merge.
    Examples: Merge Sort, Quick Sort, Binary Search.
    
    Demo: Maximum Subarray Sum (O(N log N) vs Kandane O(N)).
"""

def max_crossing_sum(arr, l, m, h):
    sm = 0
    left_sum = float('-inf')
    for i in range(m, l - 1, -1):
        sm += arr[i]
        if sm > left_sum:
            left_sum = sm
            
    sm = 0
    right_sum = float('-inf')
    for i in range(m + 1, h + 1):
        sm += arr[i]
        if sm > right_sum:
            right_sum = sm
            
    return left_sum + right_sum

def max_subarray_dc(arr, l, h):
    if l == h:
        return arr[l]
        
    m = (l + h) // 2
    return max(
        max_subarray_dc(arr, l, m),
        max_subarray_dc(arr, m + 1, h),
        max_crossing_sum(arr, l, m, h)
    )

def run_tests():
    arr = [-2, -5, 6, -2, -3, 1, 5, -6]
    # Max subarray: 6, -2, -3, 1, 5 = 7.
    assert max_subarray_dc(arr, 0, len(arr)-1) == 7
    print("[PASS] Divide and Conquer Max Subarray")

if __name__ == "__main__":
    run_tests()
