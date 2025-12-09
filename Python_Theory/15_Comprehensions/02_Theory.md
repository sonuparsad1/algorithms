# Comprehension Theory and Patterns

## Comprehension vs Loop Performance
```python
import timeit

# Loop
def with_loop():
    result = []
    for x in range(1000):
        result.append(x**2)
    return result

# Comprehension
def with_comp():
    return [x**2 for x in range(1000)]

# Comprehensions are typically faster
```

## Conditional Logic in Comprehensions
```python
# Filter (if at end)
evens = [x for x in range(10) if x % 2 == 0]

# Transform (if-else in expression)
result = ['even' if x % 2 == 0 else 'odd' for x in range(10)]

# Multiple conditions
result = [x for x in range(100) if x % 2 == 0 if x % 3 == 0]
# Same as: if x % 2 == 0 and x % 3 == 0
```

## Nested Comprehensions
```python
# Cartesian product
pairs = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(3)]
# [[1, 4], [2, 5], [3, 6]]
```

## Walrus Operator in Comprehensions (Python 3.8+)
```python
# Compute once, use multiple times
results = [(y := x**2, y+1) for x in range(5)]
# [(0, 1), (1, 2), (4, 5), (9, 10), (16, 17)]
```
