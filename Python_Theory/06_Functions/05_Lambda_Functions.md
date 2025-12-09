# Lambda Functions (Anonymous Functions)

## Definition
A **lambda function** is a small anonymous function.
- It can take any number of arguments, but can only have **one expression**.
- It returns the result of the expression automatically.

## Syntax
```python
lambda arguments: expression
```

## Examples

### 1. Basic Usage
```python
# A lambda that adds 10 to the argument
x = lambda a: a + 10
print(x(5))  # 15
```

### 2. Multiple Arguments
```python
# Multiply argument a with argument b
x = lambda a, b: a * b
print(x(5, 6))  # 30
```

## When to Use?
Lambda functions are most useful when used as an **anonymous function inside another function**, especially with higher-order functions like `map()`, `filter()`, and `reduce()`.

### Example with `filter()`
Keep only even numbers.
```python
nums = [1, 5, 4, 6, 8, 11, 3, 12]

evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens) # [4, 6, 8, 12]
```

### Example with `map()`
Double every number.
```python
nums = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, nums))
print(doubled) # [2, 4, 6, 8]
```
