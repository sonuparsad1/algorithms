# Essential Standard Library Modules

## `collections` - Specialized Containers
```python
from collections import Counter, defaultdict, deque, namedtuple

# Counter - Count occurrences
words = ['apple', 'banana', 'apple']
counts = Counter(words)  # Counter({'apple': 2, 'banana': 1})

# defaultdict - Default values for missing keys
d = defaultdict(list)
d['key'].append(1)  # No KeyError!

# deque - Double-ended queue
queue = deque([1, 2, 3])
queue.appendleft(0)  # [0, 1, 2, 3]

# namedtuple - Tuple with named fields
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x, p.y)
```

## `datetime` - Date and Time
```python
from datetime import datetime, timedelta

# Current time
now = datetime.now()

# Create specific date
date = datetime(2024, 12, 9, 14, 30)

# Arithmetic
tomorrow = now + timedelta(days=1)

# Formatting
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
```

## `itertools` - Iterator Tools
```python
import itertools

# Infinite iterators
count = itertools.count(10, 2)  # 10, 12, 14, ...
cycle = itertools.cycle([1, 2, 3])  # 1, 2, 3, 1, 2, 3, ...

# Combinatorics
perms = itertools.permutations([1, 2, 3])
combs = itertools.combinations([1, 2, 3], 2)

# Grouping
data = [('a', 1), ('a', 2), ('b', 3)]
for key, group in itertools.groupby(data, key=lambda x: x[0]):
    print(key, list(group))
```

## `functools` - Higher-Order Functions
```python
from functools import lru_cache, partial, reduce

# Caching
@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Partial application
from operator import add
add_five = partial(add, 5)
print(add_five(10))  # 15

# Reduce
numbers = [1, 2, 3, 4]
sum_all = reduce(lambda x, y: x + y, numbers)  # 10
```
