# Creating Your Own Modules

## Step 1: Create a `.py` File

**mymath.py**
```python
"""
A simple math utilities module.
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

PI = 3.14159
```

## Step 2: Import and Use

**main.py**
```python
import mymath

result = mymath.add(5, 3)
print(result)  # 8

print(mymath.PI)  # 3.14159
```

## The `__name__` Variable

```python
# mymodule.py
def greet():
    print("Hello from mymodule!")

if __name__ == "__main__":
    # This code only runs when the file is executed directly
    print("Running as script")
    greet()
else:
    # This runs when imported
    print("Imported as module")
```

**Usage:**
- `python mymodule.py` → Prints "Running as script"
- `import mymodule` → Prints "Imported as module"

## Module Attributes

Every module has special attributes:
- `__name__`: Module name
- `__file__`: File path
- `__doc__`: Docstring
- `__dict__`: Module namespace

```python
import math
print(math.__name__)  # 'math'
print(math.__doc__)   # Module documentation
```

## Best Practices

1. **One module = One responsibility**
2. **Use docstrings** for documentation
3. **Avoid global state** (mutable module-level variables)
4. **Use `if __name__ == "__main__":`** for test code
