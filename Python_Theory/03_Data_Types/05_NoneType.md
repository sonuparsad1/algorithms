# NoneType

## Definition
`None` is a special keyword in Python that represents the **absence of a value** or a **null** value. It is an object of its own datatype, the `NoneType`.

## Theory
- `None` is not the same as `0` (zero), `False`, or an empty string `""`.
- `None` is the only value of the `NoneType`.
- Functions that do not explicitly return a value return `None` by default.

## Syntax and Usage

```python
x = None

if x is None:
    print("x has no value")

if x is not None:
    print("x has a value")
```

### Important Rule: Use `is` for None
Always use `is` or `is not` to check for `None`, rather than `==` or `!=`.
- `x is None` (Correct/Pythonic)
- `x == None` (Works, but discouraged)

## Example: Default return value

```python
def my_func():
    print("Doing something")
    # No return statement here

result = my_func()
print(result)  # Output: None
```

## Common Errors
- **AttributeError**: Trying to access methods on a `None` value (often forgetting that a function returned `None`).
    ```python
    x = None
    # print(x.upper())  # AttributeError: 'NoneType' object has no attribute 'upper'
    ```
