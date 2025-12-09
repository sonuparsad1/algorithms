# Iterators and Generators

## Definition

### Iterator
An object that implements the iterator protocol (`__iter__()` and `__next__()`). Allows sequential access to elements.

### Generator
A special type of iterator created using functions with `yield`. Generates values on-the-fly, saving memory.

## Iterators

### Creating an Iterator
```python
class Counter:
    def __init__(self, max):
        self.max = max
        self.current = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        raise StopIteration

counter = Counter(3)
for num in counter:
    print(num)  # 1, 2, 3
```

### Built-in Iterators
```python
# Lists, tuples, strings are iterable
for char in "hello":
    print(char)

# iter() and next()
it = iter([1, 2, 3])
print(next(it))  # 1
print(next(it))  # 2
```

## Generators

### Generator Functions
```python
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(5):
    print(num)  # 5, 4, 3, 2, 1
```

### Generator Expressions
```python
# Like list comprehension but with ()
squares = (x**2 for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1
```

## Benefits
- **Memory Efficient**: Generate values on-demand
- **Lazy Evaluation**: Compute only when needed
- **Infinite Sequences**: Can represent infinite data
