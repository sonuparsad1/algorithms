# Practice Questions - Iterators and Generators

## Questions

### Q1: Range Generator
Implement your own `range()` function using a generator.

### Q2: Fibonacci Generator
Create a generator that yields Fibonacci numbers up to n.

### Q3: Cycle Iterator
Create an iterator that cycles through a list indefinitely.

### Q4: Filter Generator
Create a generator that filters even numbers from an iterable.

### Q5: Zip Generator
Implement your own `zip()` function using generators.

---

## Solutions

### A1: Range Generator
```python
def my_range(start, stop=None, step=1):
    if stop is None:
        start, stop = 0, start
    
    current = start
    while (step > 0 and current < stop) or (step < 0 and current > stop):
        yield current
        current += step

for num in my_range(5):
    print(num)  # 0, 1, 2, 3, 4
```

### A2: Fibonacci Generator
```python
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print(list(fibonacci(10)))
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

### A3: Cycle Iterator
```python
class Cycle:
    def __init__(self, iterable):
        self.iterable = list(iterable)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if not self.iterable:
            raise StopIteration
        value = self.iterable[self.index]
        self.index = (self.index + 1) % len(self.iterable)
        return value

cycle = Cycle([1, 2, 3])
for i, val in enumerate(cycle):
    if i >= 10:
        break
    print(val)  # 1, 2, 3, 1, 2, 3, 1, 2, 3, 1
```

### A4: Filter Generator
```python
def filter_even(iterable):
    for item in iterable:
        if item % 2 == 0:
            yield item

numbers = range(10)
evens = filter_even(numbers)
print(list(evens))  # [0, 2, 4, 6, 8]
```

### A5: Zip Generator
```python
def my_zip(*iterables):
    iterators = [iter(it) for it in iterables]
    while True:
        try:
            yield tuple(next(it) for it in iterators)
        except StopIteration:
            return

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
print(list(my_zip(list1, list2)))
# [(1, 'a'), (2, 'b'), (3, 'c')]
```
