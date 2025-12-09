# Arithmetic Operators

## Definition
Arithmetic operators are used with numeric values to perform common mathematical operations.

## List of Operators

| Operator | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| `+` | Addition | Adds two values. | `x + y` |
| `-` | Subtraction | Subtracts right operand from left. | `x - y` |
| `*` | Multiplication | Multiplies two values. | `x * y` |
| `/` | Division | Divides left by right (always returns float). | `x / y` |
| `%` | Modulus | Returns the remainder of division. | `x % y` |
| `**` | Exponentiation | Raises left operand to power of right. | `x ** y` |
| `//` | Floor Division | Divides and rounds down to nearest integer. | `x // y` |

## Code Examples

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335 (Float division)
print(a // b)  # 3 (Floor division - truncates decimal)
print(a % b)   # 1 (Remainder: 10 = 3*3 + 1)
print(a ** b)  # 1000 (10^3)
```

## Common Uses
- **Modulus (`%`)**: Checking if a number is even or odd (`x % 2 == 0`).
- **Floor Division (`//`)**: Determining how many full items fit in a container.
