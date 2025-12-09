# Membership and Identity Operators

## 1. Membership Operators
Membership operators are used to test if a sequence is presented in an object.

| Operator | Description | Example |
| :--- | :--- | :--- |
| `in` | Returns True if a sequence with the specified value is present in the object | `x in y` |
| `not in` | Returns True if a sequence with the specified value is NOT present in the object | `x not in y` |

### Examples
```python
fruits = ["apple", "banana"]

print("banana" in fruits)  # True
print("pineapple" not in fruits)  # True
print("a" in "apple")  # True (Works with strings too)
```

## 2. Identity Operators
Identity operators compare the objects, not if they are equal, but if they are actually the **same object**, with the same memory location.

| Operator | Description | Example |
| :--- | :--- | :--- |
| `is` | Returns True if both variables are the same object | `x is y` |
| `is not` | Returns True if both variables are not the same object | `x is not y` |

### `is` vs `==`
- `==` compares **value**.
- `is` compares **identity** (memory address).

```python
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)  # True (z points to the same object as x)
print(x is y)  # False (x and y are two different objects in memory)
print(x == y)  # True (x and y have the same content)
```
