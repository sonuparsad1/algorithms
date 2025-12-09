# Practice Questions - Basic Syntax

## Questions

### Q1: Variable Swapping
Create two variables `a = 50` and `b = 100`. Swap their values without using a third variable (hint: Python allows multiple assignment).

### Q2: Formatted Output
Ask the user for their name and birth year. Print a message:
`Hello [Name], you are approx [age] years old.`
(Assume current year is 2025).

### Q3: Fix the Code
```python
price = 19.99
print("The price is " + price)
```

## Solutions

**A1:**
```python
a, b = 50, 100
a, b = b, a
print(a, b)  # 100 50
```

**A2:**
```python
current_year = 2025
name = input("Enter name: ")
year_str = input("Enter birth year: ")
age = current_year - int(year_str)  # Convert input to int
print(f"Hello {name}, you are approx {age} years old.")
```

**A3:**
Error: `TypeError`, cannot concatenate float to string.
Fix:
```python
print(f"The price is {price}")
# OR
print("The price is " + str(price))
```
