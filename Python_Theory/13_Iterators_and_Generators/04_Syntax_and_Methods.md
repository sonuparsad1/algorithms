# Iterator and Generator Syntax

## Iterator Protocol
```python
class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value
```

## Generator Function Syntax
```python
def my_generator():
    yield 1
    yield 2
    yield 3

# Equivalent to
def my_generator_alt():
    return iter([1, 2, 3])
```

## Generator Expression Syntax
```python
# List comprehension (creates list)
squares_list = [x**2 for x in range(10)]

# Generator expression (creates generator)
squares_gen = (x**2 for x in range(10))
```

## `yield` vs `return`
```python
def with_return():
    return [1, 2, 3]  # Returns entire list

def with_yield():
    yield 1
    yield 2
    yield 3  # Returns generator object
```

## Generator Delegation
```python
def sub_generator():
    yield 1
    yield 2

def main_generator():
    yield from sub_generator()
    yield 3

list(main_generator())  # [1, 2, 3]
```
