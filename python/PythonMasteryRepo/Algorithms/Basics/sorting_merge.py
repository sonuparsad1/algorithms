"""
Title: Merge Sort
Topic: Algorithms Basics

Theory:
    Divide and Conquer algorithm. 
    Divides input array into two halves, calls itself for the two halves, and then merges the two sorted halves.
    
    Complexity:
    - Time: O(n log n) in all cases.
    - Space: O(n) auxiliary space (not in-place typically).
    
    Stable: Yes.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_arr = []
    i = j = 0
    
    # Merge smaller elements
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    # Append any remaining
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    
    return sorted_arr

def run_tests():
    data = [38, 27, 43, 3, 9, 82, 10]
    sorted_data = merge_sort(data)
    assert sorted_data == [3, 9, 10, 27, 38, 43, 82]
    print("[PASS] Merge Sort")

if __name__ == "__main__":
    run_tests()
