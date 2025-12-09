# Comprehension Use Cases

## Data Transformation
```python
# Convert strings to integers
strings = ['1', '2', '3']
numbers = [int(s) for s in strings]

# Extract specific fields
users = [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}]
names = [user['name'] for user in users]
```

## Filtering
```python
# Filter by condition
numbers = range(20)
evens = [x for x in numbers if x % 2 == 0]

# Filter and transform
words = ['hello', 'world', 'python']
upper_long = [w.upper() for w in words if len(w) > 5]
```

## Creating Lookup Tables
```python
# Index to value mapping
index_map = {i: chr(65+i) for i in range(26)}
# {0: 'A', 1: 'B', ..., 25: 'Z'}

# Invert dictionary
original = {'a': 1, 'b': 2}
inverted = {v: k for k, v in original.items()}
```

## Set Operations
```python
# Unique elements
numbers = [1, 2, 2, 3, 3, 4]
unique = {x for x in numbers}

# Set of squares
squares = {x**2 for x in range(10)}
```

## Generator Expressions for Memory Efficiency
```python
# Large dataset - use generator
large_data = (process(x) for x in huge_dataset)

# Process one at a time
for item in large_data:
    handle(item)
```
