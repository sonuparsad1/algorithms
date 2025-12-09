"""
Title: Selection Sort
Topic: Algorithms Basics

Theory:
    Divide array into sorted and unsorted parts.
    Repeatedly find the minimum element from unsorted part and put it at the beginning.
    
    Complexity: O(n^2) always.
    Note: Can implement unstable if not careful, but usually unstable? Actually swap usually makes it unstable.
    Pros: Minimizes number of swaps (O(n) swaps).
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap found minimum with first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def run_tests():
    data = [64, 25, 12, 22, 11]
    sorted_data = selection_sort(data.copy())
    assert sorted_data == [11, 12, 22, 25, 64]
    print("[PASS] Selection Sort")

if __name__ == "__main__":
    run_tests()
