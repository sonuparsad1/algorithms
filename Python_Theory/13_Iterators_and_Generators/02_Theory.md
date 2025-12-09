# Advanced Iterator and Generator Patterns

## `itertools` Module
```python
import itertools

# Infinite iterators
count = itertools.count(start=10, step=2)  # 10, 12, 14, ...
cycle = itertools.cycle([1, 2, 3])         # 1, 2, 3, 1, 2, 3, ...
repeat = itertools.repeat(5, times=3)      # 5, 5, 5

# Combinatoric iterators
perms = itertools.permutations([1, 2, 3])
combs = itertools.combinations([1, 2, 3], 2)

# Grouping
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

## Generator Pipelines
```python
def read_large_file(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

def filter_lines(lines, keyword):
    for line in lines:
        if keyword in line:
            yield line

def process_lines(lines):
    for line in lines:
        yield line.upper()

# Pipeline
lines = read_large_file("huge.txt")
filtered = filter_lines(lines, "ERROR")
processed = process_lines(filtered)

for line in processed:
    print(line)
```

## `yield from`
```python
def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

nested = [1, [2, 3, [4, 5]], 6]
print(list(flatten(nested)))  # [1, 2, 3, 4, 5, 6]
```

## Generator Methods
```python
def echo():
    while True:
        value = yield
        print(f"Received: {value}")

gen = echo()
next(gen)  # Prime the generator
gen.send("Hello")  # Send value
gen.close()  # Close generator
```
