# Exception Handling Syntax

## Complete Try-Except-Else-Finally
```python
try:
    # Code that might raise an exception
    result = risky_operation()
except SpecificError as e:
    # Handle specific error
    print(f"Error: {e}")
except AnotherError:
    # Handle another error
    pass
else:
    # Runs if NO exception occurred
    print("Success!")
finally:
    # ALWAYS runs
    cleanup()
```

## Assertion
```python
def calculate_average(numbers):
    assert len(numbers) > 0, "List cannot be empty"
    return sum(numbers) / len(numbers)

# Raises AssertionError if condition is False
```

## Context Manager Protocol
```python
class FileManager:
    def __init__(self, filename):
        self.filename = filename
    
    def __enter__(self):
        self.file = open(self.filename, 'r')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        return False  # Don't suppress exceptions

with FileManager("data.txt") as f:
    content = f.read()
```
