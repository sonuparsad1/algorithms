# Variables and Constants

## Definition
- **Variable**: A reserved memory location to store values. In Python, a variable is a *name* that refers to an object in memory.
- **Constant**: A type of variable whose value should not be changed. Python does not enforce constants syntactically, but by convention, uppercase names are used.

## Theory
- **Dynamic Typing**: You don't declare types (e.g., `int x`). Python infers types at runtime.
- **References**: Variables are references (pointers) to objects. If `a = [1]` and `b = a`, both point to the same list.
- **Naming Conventions**:
    - Variables: `snake_case` (e.g., `user_name`)
    - Constants: `UPPER_CASE` (e.g., `MAX_SPEED`)
    - Classes: `PascalCase` (e.g., `MyClass`)

## Syntax

```python
variable_name = value
CONSTANT_NAME = value
```

- **Multiple Assignment**: `x, y, z = 1, 2, 3`
- **Chain Assignment**: `x = y = z = 0`

## Examples

```python
# Variable assignment
age = 25
name = "John"

# Constant (Convention only)
PI = 3.14159

# Changing a variable (Dynamic typing)
x = 100       # x is an int
x = "Hello"   # x is now a str (Perfectly valid in Python)

print(name)
print(x)
```

## Common Errors
1.  **NameError**: Using a variable before assignment.
2.  **SyntaxError**: Variable names cannot start with a number (`1st_var` is invalid) or contain spaces.
