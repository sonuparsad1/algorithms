# Basic Syntax and Important Functions

## General Syntax Rules

1.  **Case Sensitivity**: Python is case-sensitive. `Variable` and `variable` are different identifiers.
2.  **Line Structure**: Newlines indicate the end of a statement. No semicolons `;` act as terminators (though using them allows multiple statements on one line, it's non-Pythonic).
3.  **Indentation**: Python uses **indentation** (whitespace) to define blocks of code (loop bodies, function bodies, conditionals).
    - Standard convention: **4 spaces** per indentation level.
    - Consistent indentation is mandatory; mixing tabs and spaces will cause errors.
4.  **Comments**:
    - Single-line: Starts with `#`.
    - Multi-line (Docstrings): Enclosed in triple quotes `'''` or `"""`.

## Important Built-in Functions (Introduction)

| Function | Description | Example |
| :--- | :--- | :--- |
| `print()` | Outputs data to the standard output device (screen). | `print("Hello")` |
| `input()` | Reads a line from standard input (keyboard) as a string. | `name = input("Enter name: ")` |
| `type()` | Returns the data type of an object. | `type(42)` -> `<class 'int'>` |
| `help()` | Invokes the built-in help system. | `help(print)` |
| `dir()` | Returns a list of attributes and methods of an object. | `dir("string")` |
| `id()` | Returns the unique identity (memory address) of an object. | `id(x)` |
| `len()` | Returns the length of an object (string, list, etc.). | `len("hello")` -> `5` |
| `range()` | Generates a sequence of numbers. | `range(5)` -> `0, 1, 2, 3, 4` |
| `int()`, `float()`, `str()` | Type conversion functions. | `int("10")` -> `10` |

## Syntax Example
```python
# This is a comment
def greet(name):
    """
    This is a docstring.
    It explains what the function does.
    """
    message = "Hello, " + name  # Indented block
    print(message)              # Indented block

greet("World")  # Function call
```

## Statements vs Expressions

### Statement
A complete line of code that performs an action.
```python
x = 5          # Assignment statement
print("Hi")    # Function call statement
if x > 3:      # Conditional statement
    pass
```

### Expression
A combination of values and operators that evaluates to a value.
```python
5 + 3          # Evaluates to 8
x > 10         # Evaluates to True or False
"Hello" * 2    # Evaluates to "HelloHello"
```

## Identifiers (Naming Rules)

### Valid Identifiers
- Must start with a letter (a-z, A-Z) or underscore `_`.
- Can contain letters, digits (0-9), and underscores.
- **Cannot** start with a digit.
- **Cannot** be a reserved keyword.

### Reserved Keywords
```python
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
#  'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
#  'try', 'while', 'with', 'yield']
```

## The `pass` Statement
A null operation. Used as a placeholder.
```python
def future_function():
    pass  # TODO: Implement later

if condition:
    pass  # Do nothing for now
```
