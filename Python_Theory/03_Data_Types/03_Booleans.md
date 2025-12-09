# Booleans

## Definition
Booleans represent one of two values: `True` or `False`. They are a subclass of integers (where True is 1 and False is 0).

## Theory
- Used primarily in **conditional statements** (if/else) and **loops**.
- Comparison operations return booleans.

```python
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
```

## Truthiness (True or False?)
In Python, almost any value is evaluated to `True` if it has some sort of content.

### What is True?
- Any non-zero number.
- Any non-empty string.
- Any non-empty list, tuple, set, or dictionary.

### What is False?
- `False` itself.
- `None`.
- Zero of any numeric type: `0`, `0.0`, `0j`.
- Empty sequences and collections: `''`, `()`, `[]`, `{}`.

## Bool Function
To check if a value acts as True or False, use the `bool()` function.

```python
print(bool("Hello"))  # True
print(bool(15))       # True

print(bool(""))       # False
print(bool(0))        # False
print(bool([]))       # False
```

## Boolean Logic Operators
`and`, `or`, `not`

```python
x = True
y = False

print(x and y)  # False
print(x or y)   # True
print(not x)    # False
```
