"""
Title: Bubble Sort
Topic: Algorithms Basics

Theory:
    Repeatedly swap adjacent elements if they are in wrong order.
    Largest elements "bubble" to the top (end) in each pass.
    
    Complexity:
    - Time: O(n^2).
    - Space: O(1).
    
    Optimization: Stop if no swaps occur in a pass.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break
    return arr

def run_tests():
    data = [64, 34, 25, 12, 22, 11, 90]
    sorted_data = bubble_sort(data.copy())
    assert sorted_data == sorted(data)
    
    print("[PASS] Bubble Sort")

if __name__ == "__main__":
    run_tests()
