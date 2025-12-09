# Common File Handling Errors

## 1. FileNotFoundError
```python
# WRONG
f = open("nonexistent.txt", "r")

# CORRECT
try:
    with open("file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("File not found")
```

## 2. Not Closing Files
```python
# WRONG
f = open("file.txt", "r")
content = f.read()
# File not closed!

# CORRECT
with open("file.txt", "r") as f:
    content = f.read()
# Automatically closed
```

## 3. Encoding Issues
```python
# WRONG
with open("file.txt", "r") as f:  # Uses system default encoding
    content = f.read()

# CORRECT
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## 4. Writing to Read-Only File
```python
# WRONG
with open("file.txt", "r") as f:
    f.write("data")  # io.UnsupportedOperation

# CORRECT
with open("file.txt", "w") as f:
    f.write("data")
```

## 5. Not Handling Permissions
```python
# WRONG
with open("/root/file.txt", "w") as f:  # PermissionError
    f.write("data")

# CORRECT
try:
    with open("/root/file.txt", "w") as f:
        f.write("data")
except PermissionError:
    print("No permission to write")
```
