# Operator Precedence

## Definition
Operator precedence describes the order in which operations are performed when there are multiple operators in an expression.

## Precedence Table (Highest to Lowest)

| Level | Operator | Description |
| :--- | :--- | :--- |
| 1 | `()` | Parentheses |
| 2 | `**` | Exponentiation |
| 3 | `+x`, `-x`, `~x` | Unary plus, Unary minus, Bitwise NOT |
| 4 | `*`, `/`, `//`, `%` | Multiplication, Division, Floor division, Modulus |
| 5 | `+`, `-` | Addition, Subtraction |
| 6 | `<<`, `>>` | Bitwise shift |
| 7 | `&` | Bitwise AND |
| 8 | `^` | Bitwise XOR |
| 9 | `\|` | Bitwise OR |
| 10 | `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` | Comparisons, Identity, Membership operators |
| 11 | `not` | Logical NOT |
| 12 | `and` | Logical AND |
| 13 | `or` | Logical OR |

## Examples

```python
result = 10 + 2 * 3
# Multiplication (*) is higher than Addition (+)
# 10 + 6
# 16
print(result)

result = (10 + 2) * 3
# Parentheses have the highest precedence
# 12 * 3
# 36
print(result)

# Right-to-left associativity for Exponentiation
print(2 ** 3 ** 2)  # 2 ** (3 ** 2) -> 2 ** 9 -> 512
```

## Tips
- When in doubt, use parentheses `()` to ensure the order of operations is what you intend. It improves readability.
