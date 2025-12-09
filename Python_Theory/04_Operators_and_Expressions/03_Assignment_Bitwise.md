# Assignment and Bitwise Operators

## 1. Assignment Operators
Used to assign values to variables.

| Operator | Description | Example | Same As |
| :--- | :--- | :--- | :--- |
| `=` | Assigns value | `x = 5` | |
| `+=` | Add AND | `x += 3` | `x = x + 3` |
| `-=` | Subtract AND | `x -= 3` | `x = x - 3` |
| `*=` | Multiply AND | `x *= 3` | `x = x * 3` |
| `/=` | Divide AND | `x /= 3` | `x = x / 3` |
| `//=` | Floor Div AND | `x //= 3` | `x = x // 3` |
| `%=` | Modulus AND | `x %= 3` | `x = x % 3` |
| `**=` | Exponent AND | `x **= 3` | `x = x ** 3` |

## 2. Bitwise Operators
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit.

| Operator | Name | Description | Example |
| :--- | :--- | :--- | :--- |
| `&` | AND | Sets each bit to 1 if both bits are 1 | `x & y` |
| `|` | OR | Sets each bit to 1 if one of two bits is 1 | `x | y` |
| `^` | XOR | Sets each bit to 1 if only one of two bits is 1 | `x ^ y` |
| `~` | NOT | Inverts all the bits | `~x` |
| `<<` | Zero fill left shift | Shift left by pushing zeros in from the right | `x << 2` |
| `>>` | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left | `x >> 2` |

### Example
```python
val = 10        # Binary: 1010
mask = 4        # Binary: 0100

print(val & mask)  # 0000 -> 0
print(val | mask)  # 1110 -> 14
print(val >> 1)    # 0101 -> 5
```
