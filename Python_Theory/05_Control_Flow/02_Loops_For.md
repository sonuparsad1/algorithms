# For Loops

## Definition
A `for` loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

## Syntax
```python
for item in sequence:
    # Code block to be executed
```

## The `range()` Function
Often used with for loops to repeat a block of code a specific number of times.
- `range(stop)`: 0 to stop-1.
- `range(start, stop)`: start to stop-1.
- `range(start, stop, step)`: increment by step.

## Examples

### 1. Iterating over a List
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
```

### 2. Iterating over a String
```python
for char in "banana":
    print(char)
```

### 3. Using `range()`
```python
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

for i in range(2, 6):
    print(i)
# Output: 2, 3, 4, 5
```

### 4. Nested Loops
A loop inside a loop.
```python
adj = ["red", "big"]
fruits = ["apple", "banana"]

for x in adj:
    for y in fruits:
        print(x, y)
```
