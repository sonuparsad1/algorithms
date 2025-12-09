# Practice Questions - Exception Handling

## Questions

### Q1: Safe Division
Write a function that safely divides two numbers, handling all possible errors.

### Q2: File Reader
Create a function that reads a file and returns its content, with proper error handling.

### Q3: Custom Exception
Create a custom `AgeError` exception and use it in an age validation function.

### Q4: Retry Decorator
Write a decorator that retries a function up to 3 times if it raises an exception.

### Q5: Context Manager
Implement a context manager for a database connection.

---

## Solutions

### A1: Safe Division
```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid types"
    except Exception as e:
        return f"Unexpected error: {e}"

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # Error: Division by zero
print(safe_divide(10, "a")) # Error: Invalid types
```

### A2: File Reader
```python
def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found"
    except PermissionError:
        return f"Error: No permission to read '{filename}'"
    except Exception as e:
        return f"Error reading file: {e}"

content = read_file_safe("data.txt")
```

### A3: Custom Exception
```python
class AgeError(Exception):
    """Raised when age is invalid"""
    pass

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("Age must be an integer")
    if age < 0:
        raise AgeError("Age cannot be negative")
    if age > 150:
        raise AgeError("Age seems unrealistic")
    return True

try:
    validate_age(-5)
except AgeError as e:
    print(f"Invalid age: {e}")
```

### A4: Retry Decorator
```python
import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise
                    print(f"Attempt {attempt + 1} failed: {e}")
                    time.sleep(delay)
        return wrapper
    return decorator

@retry(max_attempts=3)
def unreliable_function():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Failed")
    return "Success"
```

### A5: Context Manager
```python
class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        print(f"Connecting to {self.db_name}")
        self.connection = f"Connection to {self.db_name}"
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.db_name}")
        if exc_type is not None:
            print(f"Exception occurred: {exc_val}")
        return False  # Don't suppress exceptions

with DatabaseConnection("mydb") as conn:
    print(f"Using {conn}")
```
