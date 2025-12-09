"""
Title: Binary Search
Topic: Algorithms Basics

Theory:
    Divide and Conquer. Repeatedly divide the search interval in half.
    
    Pre-condition: Array MUST be sorted.
    
    Complexity:
    - Time: O(log n).
    - Space: O(1) iterative, O(log n) recursive (stack).
    
    Pitfalls:
    - Infinite loop if `mid` calculation is wrong or bounds don't update correctly.
    - Overflow: `mid = (low + high) // 2` is safe in Python (auto-large ints), 
      but `low + (high - low) // 2` is safer in fixed-width languages.
"""

def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1

def binary_search_recursive(arr, low, high, target):
    if low > high:
        return -1
    
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, mid + 1, high, target)
    else:
        return binary_search_recursive(arr, low, mid - 1, target)

def run_tests():
    data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    
    # Iterative
    assert binary_search_iterative(data, 30) == 2
    assert binary_search_iterative(data, 99) == -1
    
    # Recursive
    assert binary_search_recursive(data, 0, len(data)-1, 70) == 6
    assert binary_search_recursive(data, 0, len(data)-1, 5) == -1
    
    print("[PASS] Binary Search")

if __name__ == "__main__":
    run_tests()
