# Conditional Statements (if, elif, else)

## Definition
Conditional statements allow the program to execute certain blocks of code only if specific conditions are met.

## Syntax

```python
if condition:
    # Code to execute if condition is True
elif other_condition:
    # Code to execute if previous conditions were False and this is True
else:
    # Code to execute if all previous conditions were False
```

## Important Rules
1.  **Indentation**: The code block under the `if/elif/else` statement must be indented.
2.  **Order**: `if` comes first, `elif` is optional (can have multiple), and `else` is optional (must be last).
3.  **Conditions**: Must evaluate to a Boolean (True/False).

## Examples

### Basic If-Else
```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
```

### Multiple Conditions (Elif)
```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

### Nested If
You can have an `if` statement inside another `if` statement.

```python
x = 25

if x > 10:
    print("Above 10")
    if x > 20:
        print("and also above 20!")
```

## Short Hand If (Ternary Operator)
Write if-else in a single line.
`value_if_true if condition else value_if_false`

```python
a = 5
b = 10
print("A is greater") if a > b else print("B is greater")
```
