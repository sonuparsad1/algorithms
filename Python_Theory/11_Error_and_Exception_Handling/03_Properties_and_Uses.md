# Exception Handling Best Practices

## 1. Be Specific
```python
# BAD
try:
    # code
    pass
except:  # Catches everything, even KeyboardInterrupt!
    pass

# GOOD
try:
    # code
    pass
except ValueError:
    pass
```

## 2. Use Context Managers
```python
# Automatically handles cleanup
with open("file.txt") as f:
    content = f.read()
# File is automatically closed
```

## 3. Don't Silence Exceptions
```python
# BAD
try:
    risky_operation()
except:
    pass  # Silent failure!

# GOOD
try:
    risky_operation()
except Exception as e:
    logger.error(f"Operation failed: {e}")
    raise
```

## 4. EAFP vs LBYL

### EAFP (Easier to Ask Forgiveness than Permission)
```python
# Pythonic
try:
    value = my_dict[key]
except KeyError:
    value = default
```

### LBYL (Look Before You Leap)
```python
# Less Pythonic
if key in my_dict:
    value = my_dict[key]
else:
    value = default
```
