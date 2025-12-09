# Comprehensions in Python

## Definition

**Comprehensions** provide a concise way to create sequences (lists, sets, dictionaries) from existing iterables. They're more readable and often faster than traditional loops.

## List Comprehensions
```python
# Traditional loop
squares = []
for x in range(10):
    squares.append(x**2)

# List comprehension
squares = [x**2 for x in range(10)]
```

### With Condition
```python
# Even numbers only
evens = [x for x in range(20) if x % 2 == 0]

# With if-else
result = [x if x % 2 == 0 else -x for x in range(10)]
```

### Nested Comprehensions
```python
# Flatten 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6]

# Create 2D list
matrix = [[i*j for j in range(3)] for i in range(3)]
```

## Set Comprehensions
```python
# Unique squares
unique_squares = {x**2 for x in [1, 1, 2, 2, 3, 3]}
# {1, 4, 9}
```

## Dictionary Comprehensions
```python
# Square dictionary
squares_dict = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Swap keys and values
original = {'a': 1, 'b': 2}
swapped = {v: k for k, v in original.items()}
# {1: 'a', 2: 'b'}
```

## Generator Expressions
```python
# Like list comprehension but with ()
gen = (x**2 for x in range(10))
# Returns generator object, not list
```
