"""
Title: Linear Search
Topic: Algorithms Basics

Theory:
    Simplest search algorithm. Iterate through the list until target is found.
    
    Complexity:
    - Time: O(n) worst case.
    - Space: O(1).
    
    Data Requirements:
    - Data does NOT need to be sorted.
"""

def linear_search(arr, target):
    """
    Returns index of target if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def run_tests():
    data = [10, 50, 30, 70, 80, 20]
    
    assert linear_search(data, 30) == 2
    assert linear_search(data, 99) == -1
    assert linear_search([], 1) == -1
    
    print("[PASS] Linear Search")

if __name__ == "__main__":
    run_tests()
