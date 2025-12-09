# Lists - Theory and Operations

## Creating Lists
```python
# Empty list
empty = []

# List with items
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# List comprehension
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
```

## List Methods

### Adding Elements
```python
fruits = ["apple", "banana"]

fruits.append("cherry")       # Add to end
fruits.insert(1, "orange")    # Insert at index
fruits.extend(["grape", "kiwi"])  # Add multiple
```

### Removing Elements
```python
fruits.remove("banana")  # Remove first occurrence
popped = fruits.pop()    # Remove and return last item
popped = fruits.pop(0)   # Remove and return at index
fruits.clear()           # Remove all
```

### Other Methods
```python
numbers = [3, 1, 4, 1, 5]

numbers.sort()           # Sort in place
numbers.reverse()        # Reverse in place
count = numbers.count(1) # Count occurrences
index = numbers.index(4) # Find index
```

## List Slicing
```python
nums = [0, 1, 2, 3, 4, 5]

print(nums[1:4])    # [1, 2, 3]
print(nums[:3])     # [0, 1, 2]
print(nums[3:])     # [3, 4, 5]
print(nums[::2])    # [0, 2, 4] (every 2nd)
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] (reverse)
```

## List Copying
```python
original = [1, 2, 3]

# Shallow copy
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# Deep copy (for nested lists)
import copy
nested = [[1, 2], [3, 4]]
deep = copy.deepcopy(nested)
```
