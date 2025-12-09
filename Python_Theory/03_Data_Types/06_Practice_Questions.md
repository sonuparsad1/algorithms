# Practice Questions - Data Types

## Questions

### Q1: Type Identification
What is the data type of the following values?
1. `x = 5`
2. `x = 5.0`
3. `x = 5 > 4`
4. `x = "5"`
5. `x = int("5")`

### Q2: Immutability
What happens if you run the following code? Why?
```python
x = (1, 2)
x[0] = 5
```

### Q3: Casting Challenge
Convert the float number `8.99` to an integer. What is the result: `8` or `9`?

### Q4: Boolean Logic
Evaluate:
`True and False or not False`

---

## Solutions

**A1:**
1. `int`
2. `float`
3. `bool` (`True`)
4. `str`
5. `int`

**A2:**
**TypeError**. Tuples are immutable; you cannot change elements after creation.

**A3:**
Result is `8`. Casting `int(8.99)` truncates the decimal part; it does not round.

**A4:**
Order of operations: `not` -> `and` -> `or`.
1. `not False` -> `True`
2. `True and False` -> `False`
3. `False or True` -> `True`
Final Answer: `True`
