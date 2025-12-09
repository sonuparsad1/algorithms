# Common Iterator and Generator Errors

## 1. Exhausted Generator
```python
# WRONG
gen = (x for x in range(3))
list(gen)  # [0, 1, 2]
list(gen)  # [] - Generator exhausted!

# CORRECT - Create new generator or use list
data = list(range(3))
```

## 2. Forgetting to Call `next()` or Iterate
```python
# WRONG
gen = (x for x in range(3))
print(gen)  # <generator object>

# CORRECT
for x in gen:
    print(x)
```

## 3. StopIteration Not Handled
```python
# WRONG
it = iter([1, 2])
next(it)
next(it)
next(it)  # StopIteration!

# CORRECT
it = iter([1, 2])
try:
    while True:
        print(next(it))
except StopIteration:
    pass
```

## 4. Modifying List While Iterating
```python
# WRONG
numbers = [1, 2, 3, 4]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Modifies during iteration!

# CORRECT
numbers = [num for num in numbers if num % 2 != 0]
```

## 5. Not Returning `self` in `__iter__`
```python
# WRONG
class MyIterator:
    def __iter__(self):
        return None  # Should return self!

# CORRECT
class MyIterator:
    def __iter__(self):
        return self
```
