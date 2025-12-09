# Common Operations and Syntax

## List Comprehensions
```python
# Basic
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## Dictionary Comprehensions
```python
# Basic
squares_dict = {x: x**2 for x in range(5)}

# From two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
```

## Set Comprehensions
```python
unique_squares = {x**2 for x in [1, 1, 2, 2, 3, 3]}
```

## Nested Structures
```python
# List of dictionaries
students = [
    {"name": "Alice", "grade": 90},
    {"name": "Bob", "grade": 85}
]

# Dictionary of lists
grades = {
    "Alice": [90, 85, 92],
    "Bob": [88, 90, 87]
}
```

## Common Patterns
```python
# Enumerate
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# Zip
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# Sorted
sorted_list = sorted([3, 1, 4, 1, 5])
sorted_dict = sorted(d.items(), key=lambda x: x[1])
```
