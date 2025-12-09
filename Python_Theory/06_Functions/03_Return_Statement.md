# Return Statement

## Definition
The `return` statement is used to exit a function and go back to the place from where it was called.

## Usage
- **Returning a value**: `return result`
- **Returning `None`**: If `return` is omitted or used without a value, the function returns `None`.
- **Exiting early**: `return` can be used to stop function execution based on a condition.

## Multiple Return Values
Python allows returning multiple values. It effectively packs them into a **tuple**.

```python
def get_user():
    name = "John"
    age = 30
    return name, age

name, age = get_user()
print(name) # John
```

## Examples

### Basic Return
```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result) # 8
```

### Early Exit
```python
def absolute_value(num):
    if num >= 0:
        return num
    return -num

print(absolute_value(-10)) # 10
```
