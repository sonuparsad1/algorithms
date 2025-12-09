# Common Comprehension Errors

## 1. Too Complex
```python
# WRONG - Hard to read
result = [x**2 if x % 2 == 0 else x**3 if x % 3 == 0 else x 
          for x in range(100) if x > 10 if x < 90]

# CORRECT - Use regular loop for complex logic
result = []
for x in range(11, 90):
    if x % 2 == 0:
        result.append(x**2)
    elif x % 3 == 0:
        result.append(x**3)
    else:
        result.append(x)
```

## 2. Modifying List While Iterating
```python
# WRONG
numbers = [1, 2, 3, 4]
[numbers.remove(x) for x in numbers if x % 2 == 0]  # Unpredictable!

# CORRECT
numbers = [x for x in numbers if x % 2 != 0]
```

## 3. Using List Comp for Side Effects
```python
# WRONG - Comprehensions should create new data
[print(x) for x in range(10)]  # Creates useless list of None

# CORRECT
for x in range(10):
    print(x)
```

## 4. Forgetting Parentheses for Generator
```python
# List (memory intensive)
big_list = [x**2 for x in range(1000000)]

# Generator (memory efficient)
big_gen = (x**2 for x in range(1000000))
```

## 5. Nested Comprehension Confusion
```python
# Order matters!
# for x in range(3) for y in range(3)
# is NOT the same as
# for y in range(3) for x in range(3)

pairs1 = [(x, y) for x in range(3) for y in range(3)]
# [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
```
