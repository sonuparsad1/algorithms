"""
Title: Quick Sort
Topic: Algorithms Basics

Theory:
    Divide and Conquer.
    Picks an element as pivot and partitions the given array around the picked pivot.
    
    Partitions:
    1. Lomuto: Pivot is typically last element. Easier to implement.
    2. Hoare: Pivot is typically first/last. Faster in practice (fewer swaps).

    Complexity:
    - Time: O(n log n) average, O(n^2) worst case.
    - Space: O(log n) stack space.
    
    Not Stable.
"""

import random

def quick_sort(arr):
    """Recursive Quick Sort using Python list comprehensions (Not efficient space-wise but readable)."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# ==========================================
# In-Place Implementation (Lomuto)
# ==========================================

def quick_sort_inplace(arr, low, high):
    if low < high:
        pi = partition_lomuto(arr, low, high)
        quick_sort_inplace(arr, low, pi - 1)
        quick_sort_inplace(arr, pi + 1, high)

def partition_lomuto(arr, low, high):
    pivot = arr[high]
    i = (low - 1)
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def run_tests():
    data = [10, 7, 8, 9, 1, 5]
    
    # 1. Pythonic
    res = quick_sort(data)
    assert res == [1, 5, 7, 8, 9, 10]
    
    # 2. In-Place
    data_copy = data.copy()
    quick_sort_inplace(data_copy, 0, len(data_copy)-1)
    assert data_copy == [1, 5, 7, 8, 9, 10]
    
    print("[PASS] Quick Sort")

if __name__ == "__main__":
    run_tests()
