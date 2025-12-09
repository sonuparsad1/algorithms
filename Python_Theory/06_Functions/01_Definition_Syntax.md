# Functions Definition and Syntax

## Definition
A **function** is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reusing.

## Theory
- **Abstractions**: Functions allow you to abstract logic. Instead of repeating 10 lines of code, you call a function once.
- **Maintainability**: If you need to change logic, you only change it in one place (the function definition).

## Syntax
- Defined using the `def` keyword.
- Function name should follow variable naming conventions (snake_case).
- Parentheses `()` allow passing parameters.
- A colon `:` starts the function block.
- The function body must be indented.
- An optional `return` statement exits the function, passing back a value.

```python
def function_name(parameters):
    """docstring"""
    # statement(s)
    return expression
```

## First Function Example

```python
# Definition
def say_hello():
    print("Hello from a function")

# Calling the function
say_hello()
```

## Pass by Object Reference
Python uses a mechanism known as "Call by Object Reference".
- If you pass an **immutable** object (int, str, tuple), the function cannot modify the original object.
- If you pass a **mutable** object (list, dict), the function *can* modify the contents of the object.
