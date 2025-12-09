"""
Title: Heap Sort
Topic: Algorithms Basics

Theory:
    Comparison based sorting technique based on Binary Heap data structure.
    Usually we build a Max-Heap then extract elements one by one.
    
    Complexity:
    - Time: O(n log n).
    - Space: O(1) in-place.
    
    Not stable.
"""

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    
    # Build max heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
        
    # One by one extract elements
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]
        # Call max heapify on reduced heap
        heapify(arr, i, 0)
    
    return arr

def run_tests():
    data = [12, 11, 13, 5, 6, 7]
    sorted_arr = heap_sort(data.copy())
    assert sorted_arr == [5, 6, 7, 11, 12, 13]
    print("[PASS] Heap Sort")

if __name__ == "__main__":
    run_tests()
