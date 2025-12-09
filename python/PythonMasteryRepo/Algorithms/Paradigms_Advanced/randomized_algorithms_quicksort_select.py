"""
Title: Randomized Algorithms (Quickselect)
Topic: Paradigms

Theory:
    Quickselect: Find kth smallest element in O(N) average.
    Uses Random Pivot Partitioning.
"""

import random

def partition(arr, l, r):
    pivot_idx = random.randint(l, r)
    arr[r], arr[pivot_idx] = arr[pivot_idx], arr[r]
    pivot = arr[r]
    
    i = l
    for j in range(l, r):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def quickselect(arr, l, r, k):
    if l <= r:
        pi = partition(arr, l, r)
        
        if pi == k:
            return arr[pi]
        elif pi < k:
            return quickselect(arr, pi + 1, r, k)
        else:
            return quickselect(arr, l, pi - 1, k)
    return None

def run_tests():
    arr = [10, 4, 5, 8, 6, 11, 26]
    # Sorted: 4, 5, 6, 8, 10, 11, 26
    # k=0 (smallest) -> 4
    # k=3 (4th smallest) -> 8
    
    assert quickselect(arr.copy(), 0, len(arr)-1, 0) == 4
    assert quickselect(arr.copy(), 0, len(arr)-1, 3) == 8
    
    print("[PASS] Quickselect")

if __name__ == "__main__":
    run_tests()
