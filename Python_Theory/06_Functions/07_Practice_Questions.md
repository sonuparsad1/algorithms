# Practice Questions - Functions

## Questions

### Q1: Calculator Function
Write a function `calculate(a, b, operation)` where `operation` is a string (`add`, `sub`). It should return the result.

### Q2: Lambda Sort
Given a list of tuples: `points = [(1, 2), (3, 1), (5, 0)]`.
use a lambda function to sort this list by the *second* element of each tuple.

### Q3: Factorial Recursion
Write a recursive function that returns the sum of natural numbers up to `n`. `sum(3) -> 3+2+1 = 6`.

### Q4: Default Arguments
Define a function `greet(name, msg="Good morning!")`. Call it in two ways: once with just a name, and once with a name and a custom message.

### Q5: Scope Debug
What is the output of this code?
```python
x = 10
def change():
    x = 20
change()
print(x)
```

---

## Solutions

**A1:**
```python
def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "sub":
        return a - b

print(calculate(10, 5, "add")) # 15
```

**A2:**
```python
points = [(1, 2), (3, 1), (5, 0)]
points.sort(key=lambda x: x[1])
print(points)
# Output: [(5, 0), (3, 1), (1, 2)]
```

**A3:**
```python
def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)
```

**A4:**
```python
greet("Alice")
greet("Bob", "How are you?")
```

**A5:**
`10`. The function `change()` creates a *local* variable `x` and sets it to 20. It does not affect the *global* `x`.
