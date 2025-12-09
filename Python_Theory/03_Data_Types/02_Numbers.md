# Numbers

## Definition
Python supports three distinct numeric types:
1.  **Integers** (`int`)
2.  **Floating point numbers** (`float`)
3.  **Complex numbers** (`complex`)

## 1. Integers (`int`)
- Whole numbers, positive or negative, without decimals, of unlimited length.
- Python 3 handles large integers automatically (no "long" type like in Python 2 or C).

```python
x = 1
y = 35656222554887711
z = -3255522

print(type(x))  # <class 'int'>
```

## 2. Floating Point Numbers (`float`)
- Numbers containing one or more decimals.
- Can also be scientific numbers with an "e" to indicate the power of 10.

```python
x = 1.10
y = 1.0
z = -35.59
w = 35e3        # 35 * 10^3 = 35000.0
# Note: w is a float
```

## 3. Complex Numbers (`complex`)
- Written with a "j" as the imaginary part.
- Useful in engineering and complex mathematics.

```python
x = 3+5j
y = 5j
z = -5j

print(type(x))  # <class 'complex'>
print(x.real)   # 3.0
print(x.imag)   # 5.0
```

## Useful Math Functions

### Built-in
- `abs(x)`: Absolute value.
- `round(x, n)`: Round number to `n` digits.
- `pow(x, y)`: x to the power of y (same as `x ** y`).

### The `math` Module
For more advanced operations, import `math`.

```python
import math

print(math.ceil(1.4))   # 2
print(math.floor(1.4))  # 1
print(math.sqrt(64))    # 8.0
print(math.pi)          # 3.14159...
```

## Common Errors
- **Float Precision**: Floats are approximations. `0.1 + 0.2` might equal `0.30000000000000004` instead of `0.3` due to binary floating-point representation.
- **Division**: In Python 3, `/` always returns a float (`a / b`). Use `//` for integer (floor) division.
