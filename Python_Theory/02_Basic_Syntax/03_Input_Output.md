# Input and Output

## Output: `print()`
The `print()` function sends data to the standard output.

### key Arguments
- `sep`: Separator between items (default is space `' '`).
- `end`: What to print at the end (default is newline `'\n'`).

### Examples
```python
print("Hello", "World")             # Output: Hello World
print("Hello", "World", sep="-")    # Output: Hello-World
print("Line 1", end=" ")
print("Line 2")                     # Output: Line 1 Line 2
```

## Input: `input()`
The `input()` function pauses execution and waits for the user to type text and press Enter.
**Important**: It *always* returns a **string**.

### Syntax
```python
variable = input("Prompt message: ")
```

### Type Casting
If you need a number, you must cast the string.
```python
age = input("Enter age: ")  # "25"
age_int = int(age)          # 25
```

## String Formatting (Output Formatting)
The modern way to format strings is using **f-strings** (formatted string literals), introduced in Python 3.6.

```python
name = "Alice"
score = 95
print(f"Player {name} scored {score} points.")
```

Other methods (older):
- `.format()`: `"Player {} scored {}".format(name, score)`
- `%` operator: `"Player %s scored %d" % (name, score)`
