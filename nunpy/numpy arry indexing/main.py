"""
=============================================================================
                    NUMPY ARRAY INDEXING - COMPLETE GUIDE
=============================================================================
Indexing is the method to select a single or a group of elements from an array.
NumPy offers various indexing techniques for different use cases.
=============================================================================
"""

import numpy as np

# =============================================================================
# 1. BASIC INDEXING (Access single elements)
# =============================================================================
print("=" * 75)
print("1. BASIC INDEXING - Access single elements")
print("=" * 75)

# 1D Array
arr1d = np.array([10, 20, 30, 40, 50])
print(f"\n1D Array: {arr1d}")
print(f"First element (index 0): {arr1d[0]}")      # Output: 10
print(f"Second element (index 1): {arr1d[1]}")     # Output: 20
print(f"Element at index 3: {arr1d[3]}")           # Output: 40

# 2D Array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{arr2d}")
print(f"Element at row 0, col 1: {arr2d[0, 1]}")   # Output: 2
print(f"Element at row 2, col 2: {arr2d[2, 2]}")   # Output: 9

# 3D Array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"\n3D Array:\n{arr3d}")
print(f"Element at [0, 1, 0]: {arr3d[0, 1, 0]}")   # Output: 3
print(f"Element at [1, 0, 1]: {arr3d[1, 0, 1]}")   # Output: 6

# =============================================================================
# 2. NEGATIVE INDEXING (Access from the end)
# =============================================================================
print("\n" + "=" * 75)
print("2. NEGATIVE INDEXING - Count from the end (last element is -1)")
print("=" * 75)

arr = np.array([10, 20, 30, 40, 50])
print(f"\nArray: {arr}")
print(f"Last element (index -1): {arr[-1]}")       # Output: 50
print(f"Second last element (index -2): {arr[-2]}") # Output: 40

print(f"\n2D Array:\n{arr2d}")
print(f"Last element of last row: {arr2d[-1, -1]}") # Output: 9
print(f"First element of last row: {arr2d[-1, 0]}") # Output: 7

# =============================================================================
# 3. SLICING (Extract a range of elements)
# =============================================================================
print("\n" + "=" * 75)
print("3. SLICING - Extract consecutive elements (start:stop:step)")
print("=" * 75)

arr = np.array([10, 20, 30, 40, 50, 60, 70])
print(f"\nArray: {arr}")
print(f"arr[1:4] (elements at index 1, 2, 3): {arr[1:4]}")        # [20 30 40]
print(f"arr[::2] (every 2nd element): {arr[::2]}")                # [10 30 50 70]
print(f"arr[::-1] (reverse array): {arr[::-1]}")                  # [70 60 50 40 30 20 10]
print(f"arr[2:] (from index 2 to end): {arr[2:]}")                # [30 40 50 60 70]
print(f"arr[:3] (first 3 elements): {arr[:3]}")                   # [10 20 30]

# 2D Slicing
print(f"\n2D Array:\n{arr2d}")
print(f"arr2d[0:2, 1:3] (rows 0-1, columns 1-2):\n{arr2d[0:2, 1:3]}")  # [[2 3]
                                                                       #  [5 6]]
print(f"arr2d[:, 1] (all rows, column 1): {arr2d[:, 1]}")         # [2 5 8]
print(f"arr2d[1, :] (row 1, all columns): {arr2d[1, :]}")         # [4 5 6]

# =============================================================================
# 4. BOOLEAN INDEXING (Filter elements using conditions)
# =============================================================================
print("\n" + "=" * 75)
print("4. BOOLEAN INDEXING - Select elements matching a condition")
print("=" * 75)

arr = np.array([10, 20, 30, 40, 50, 60])
print(f"\nArray: {arr}")
print(f"Elements > 30: {arr[arr > 30]}")            # [40 50 60]
print(f"Elements == 30: {arr[arr == 30]}")          # [30]
print(f"Elements <= 25: {arr[arr <= 25]}")          # [10 20]

# Multiple conditions (use & for AND, | for OR)
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{arr2d}")
print(f"Elements > 2 AND < 8: {arr2d[(arr2d > 2) & (arr2d < 8)]}")  # [3 4 5 6 7]
print(f"Elements == 2 OR == 5: {arr2d[(arr2d == 2) | (arr2d == 5)]}")  # [2 5]
print(f"Even elements (% 2 == 0): {arr2d[arr2d % 2 == 0]}")        # [2 4 6 8]

# =============================================================================
# 5. FANCY INDEXING (Access multiple elements using index arrays)
# =============================================================================
print("\n" + "=" * 75)
print("5. FANCY INDEXING - Access elements using index lists/arrays")
print("=" * 75)

arr = np.array([10, 20, 30, 40, 50])
print(f"\nArray: {arr}")
indices = [0, 2, 4]
print(f"Access indices [0, 2, 4]: {arr[indices]}")  # [10 30 50]

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\n2D Array:\n{arr2d}")
row_indices = [0, 1, 2]
col_indices = [2, 1, 0]
print(f"Fancy index with row_indices=[0,1,2], col_indices=[2,1,0]:")
print(f"Elements: {arr2d[row_indices, col_indices]}")  # [3 5 7]

# =============================================================================
# 6. ELLIPSIS (...) INDEXING (Represent multiple colons)
# =============================================================================
print("\n" + "=" * 75)
print("6. ELLIPSIS (...) INDEXING - Shorthand for multiple colons")
print("=" * 75)

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"\n3D Array shape (2, 2, 3):\n{arr3d}")
print(f"arr3d[..., 0] (all elements, last column): {arr3d[..., 0]}")  # [[1 4] [7 10]]
print(f"arr3d[1, ...] (last block, all elements):\n{arr3d[1, ...]}")  # [[7 8 9] [10 11 12]]
print(f"arr3d[..., 1] (all elements, middle column): {arr3d[..., 1]}")  # [[2 5] [8 11]]

# =============================================================================
# 7. MODIFYING ELEMENTS (Update array values using indexing)
# =============================================================================
print("\n" + "=" * 75)
print("7. MODIFYING ELEMENTS - Update values using indexing")
print("=" * 75)

# Single element
arr = np.array([10, 20, 30, 40, 50])
print(f"\nOriginal 1D: {arr}")
arr[2] = 999
print(f"After arr[2] = 999: {arr}")

# Multiple elements via slicing
arr = np.array([10, 20, 30, 40, 50])
arr[1:4] = [100, 200, 300]
print(f"After arr[1:4] = [100, 200, 300]: {arr}")

# 2D modification
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"\nOriginal 2D:\n{arr2d}")
arr2d[1, :] = [40, 50, 60]
print(f"After arr2d[1, :] = [40, 50, 60]:\n{arr2d}")

# Boolean indexing modification
arr = np.array([10, 20, 30, 40, 50])
arr[arr > 25] = 999
print(f"\nModify elements > 25 to 999: {arr}")

# =============================================================================
# 8. COPY VS VIEW (Understanding data relationships)
# =============================================================================
print("\n" + "=" * 75)
print("8. COPY VS VIEW - Understanding reference vs independent copy")
print("=" * 75)

original = np.array([1, 2, 3, 4, 5])

# View (reference to original data)
view = original[1:4]
print(f"\nOriginal: {original}")
print(f"View (view = original[1:4]): {view}")
original[2] = 999
print(f"After original[2] = 999:")
print(f"  Original: {original}")
print(f"  View: {view}")  # View reflects the change!

# Copy (independent data)
original = np.array([1, 2, 3, 4, 5])
copy = original[1:4].copy()
print(f"\nOriginal: {original}")
print(f"Copy (copy = original[1:4].copy()): {copy}")
original[2] = 999
print(f"After original[2] = 999:")
print(f"  Original: {original}")
print(f"  Copy: {copy}")  # Copy is unchanged!

# =============================================================================
# 9. ADVANCED COMBINATIONS (Mix different indexing methods)
# =============================================================================
print("\n" + "=" * 75)
print("9. ADVANCED COMBINATIONS - Mix different indexing techniques")
print("=" * 75)

arr3d = np.arange(24).reshape(2, 3, 4)
print(f"\n3D Array shape (2, 3, 4):\n{arr3d}")

# Slice + basic indexing
print(f"\narr3d[0, 1:, 2] (block 0, rows 1+, col 2): {arr3d[0, 1:, 2]}")

# Slice + fancy indexing
print(f"arr3d[0, [0, 2], 1:3]:\n{arr3d[0, [0, 2], 1:3]}")

# Boolean + slicing
arr = np.array([10, 20, 30, 40, 50, 60])
mask = arr > 20
print(f"\nArray: {arr}")
print(f"Elements > 20, then reverse: {arr[mask][::-1]}")

print("\n" + "=" * 75)
print("INDEXING REFERENCE COMPLETE")
print("=" * 75)