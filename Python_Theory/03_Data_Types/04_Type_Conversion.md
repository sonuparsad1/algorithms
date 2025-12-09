# Type Conversion (Casting)

## Definition
Type conversion is the process of converting the value of one data type (integer, string, float, etc.) to another data type.

## 1. Implicit Conversion
Python automatically converts one data type to another without any user involvement. This usually happens when mixing types to prevent data loss.

```python
x_int = 10
y_float = 10.5

result = x_int + y_float

print(result)        # 20.5
print(type(result))  # <class 'float'>
# Python promoted the int to float to perform the addition.
```

## 2. Explicit Conversion (Casting)
The user manually changes the data type using built-in functions like `int()`, `float()`, `str()`, etc.

### Common Functions

- `int(x)`: Converts x to an integer.
    - `int(3.9)` -> `3` (truncates, does not round)
    - `int("10")` -> `10`
    - `int("10.5")` -> Error! (String must look like an int)

- `float(x)`: Converts x to a float.
    - `float(5)` -> `5.0`
    - `float("3.14")` -> `3.14`

- `str(x)`: Converts x to a string representation.
    - `str(100)` -> `"100"`
    - `str([1, 2])` -> `"[1, 2]"`

### Examples

```python
# Convert float to int
num_sum = int(123.654)
print(num_sum)  # 123 (truncation)

# Convert number to string for concatenation
age = 25
message = "I am " + str(age) + " years old"
print(message)
```

## Common Errors
- **ValueError**: Trying to cast an incompatible string to a number.
  ```python
  x = int("Hello")  # ValueError: invalid literal for int()
  y = int("12.5")   # ValueError: invalid literal for int() (must convert to float first, then int)
  ```
