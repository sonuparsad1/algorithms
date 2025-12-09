# Scope and Lifetime

## Definition
- **Scope**: The region of code where a variable is defined and can be accessed.
- **Lifetime**: How long a variable exists in memory.

## Types of Scope (LEGB Rule)
Python resolves names using the LEGB rule:
1.  **L**ocal: Defined inside function/class.
2.  **E**nclosing: Defined in enclosing functions (nested functions).
3.  **G**lobal: Defined at the uppermost level.
4.  **B**uilt-in: Reserved names in Python modules (e.g., `print`, `len`).

## Global vs Local

### Local Scope
Variables created inside a function are local to it.
```python
def my_func():
    x = 10  # Local scope
    print(x)

my_func()
# print(x) # NameError: name 'x' is not defined
```

### Global Scope
Variables created outside functions are global.
```python
x = 100 # Global

def my_func():
    print(x) # Access global x

my_func()
```

## The `global` Keyword
To modify a global variable inside a function, use `global`.
```python
count = 0

def increment():
    global count
    count += 1

increment()
print(count) # 1
```

## Common Errors
- **UnboundLocalError**: Trying to modify a global variable inside a function without declaring it global, but treating it like a local variable.
    ```python
    x = 10
    def broken():
        print(x) # Errors here because Python sees assignment below and thinks x is local
        x = 5
    ```
