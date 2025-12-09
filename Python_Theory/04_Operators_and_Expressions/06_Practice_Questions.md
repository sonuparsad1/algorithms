# Practice Questions - Operators

## Questions

### Q1: Arithmetic
Calculate `25 // 4` and `25 % 4`. Explain the results.

### Q2: Logic Check
What is the result of `False or (True and False)`?

### Q3: Identity
```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b)
```
What will the two print statements output?

### Q4: Precedence
Evaluate: `3 * 1 ** 3`.

### Q5: Membership
How do you check if the character "z" is NOT present in the string "Python"?

---

## Solutions

**A1:**
- `25 // 4` -> `6` (Integer division, goes in 6 times)
- `25 % 4` -> `1` (Remainder is 1)

**A2:**
`False`.
1. `(True and False)` -> `False`
2. `False or False` -> `False`

**A3:**
- `True` (Values are equal)
- `False` (Different objects in memory). `[1, 2, 3]` creates a new list each time.

**A4:**
`3`.
Exponentiation (`**`) has higher precedence than multiplication (`*`).
1. `1 ** 3` -> `1`
2. `3 * 1` -> `3`

**A5:**
```python
"z" not in "Python"  # Returns True
```
