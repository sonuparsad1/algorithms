# Common Exception Handling Errors

## 1. Catching Too Broad
```python
# WRONG
try:
    value = int(input())
except:  # Catches KeyboardInterrupt, SystemExit, etc.
    pass

# CORRECT
try:
    value = int(input())
except ValueError:
    pass
```

## 2. Empty Except Block
```python
# WRONG
try:
    risky_code()
except Exception:
    pass  # Silently fails!

# CORRECT
try:
    risky_code()
except Exception as e:
    logger.error(f"Error: {e}")
```

## 3. Not Using Finally for Cleanup
```python
# WRONG
file = open("data.txt")
try:
    process(file)
except:
    pass
file.close()  # Might not execute if exception occurs!

# CORRECT
file = open("data.txt")
try:
    process(file)
finally:
    file.close()  # Always executes

# BETTER
with open("data.txt") as file:
    process(file)
```

## 4. Raising Wrong Exception Type
```python
# WRONG
def divide(a, b):
    if b == 0:
        raise Exception("Division by zero")  # Too generic

# CORRECT
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
```
