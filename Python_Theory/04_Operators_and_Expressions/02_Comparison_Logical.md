# Comparison and Logical Operators

## 1. Comparison Operators
Comparison operators are used to compare two values. They **always** return a Boolean value (`True` or `False`).

| Operator | Name | Example |
| :--- | :--- | :--- |
| `==` | Equal | `x == y` |
| `!=` | Not Equal | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal to | `x >= y` |
| `<=` | Less than or equal to | `x <= y` |

### Chained Comparison
Python supports chained comparisons, which is a unique feature.
```python
x = 5
print(1 < x < 10)  # True (Equivalent to: 1 < x and x < 10)
```

## 2. Logical Operators
Logical operators are used to combine conditional statements.

| Operator | Description | Example |
| :--- | :--- | :--- |
| `and` | Returns True if both statements are true | `x < 5 and  x < 10` |
| `or` | Returns True if one of the statements is true | `x < 5 or x < 4` |
| `not` | Reverse the result, returns False if the result is true | `not(x < 5 and x < 10)` |

### Short-Circuit Evaluation
- `and`: If the first operand is False, Python doesn't check the second operand; returns False immediately.
- `or`: If the first operand is True, Python doesn't check the second operand; returns True immediately.

```python
x = 10
# 'x > 20' is False, so execution stops there. 
# Safe because 10/0 would raise ZeroDivisionError if evaluated.
if x > 20 and (10 / 0) == 1:
    print("This won't print")
else:
    print("Safe")
```
