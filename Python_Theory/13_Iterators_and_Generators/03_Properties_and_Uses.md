# Iterator and Generator Use Cases

## Memory-Efficient Data Processing
```python
# BAD - Loads entire file into memory
def process_file_bad(filename):
    with open(filename) as f:
        lines = f.readlines()  # All lines in memory!
    return [line.upper() for line in lines]

# GOOD - Processes line by line
def process_file_good(filename):
    with open(filename) as f:
        for line in f:  # Generator!
            yield line.upper()
```

## Infinite Sequences
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Get first 10 Fibonacci numbers
fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
```

## Custom Range
```python
def custom_range(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

for num in custom_range(0, 10, 2):
    print(num)  # 0, 2, 4, 6, 8
```

## Stateful Iteration
```python
def moving_average(data, window_size):
    window = []
    for value in data:
        window.append(value)
        if len(window) > window_size:
            window.pop(0)
        yield sum(window) / len(window)

data = [1, 2, 3, 4, 5]
for avg in moving_average(data, 3):
    print(f"{avg:.2f}")
```
