# File Handling in Python

## Definition

**File handling** allows programs to create, read, update, and delete files. Python provides built-in functions for working with files.

## File Modes

| Mode | Description |
|------|-------------|
| `'r'` | Read (default) - Error if file doesn't exist |
| `'w'` | Write - Creates new file or overwrites existing |
| `'a'` | Append - Creates new file or appends to existing |
| `'x'` | Exclusive creation - Error if file exists |
| `'r+'` | Read and write |
| `'b'` | Binary mode (e.g., `'rb'`, `'wb'`) |
| `'t'` | Text mode (default) |

## Basic File Operations

### Opening and Closing
```python
# Manual close
file = open("data.txt", "r")
content = file.read()
file.close()

# Using with statement (RECOMMENDED)
with open("data.txt", "r") as file:
    content = file.read()
# File automatically closed
```

## File Object Methods

### Reading
```python
with open("data.txt", "r") as f:
    content = f.read()        # Read entire file
    line = f.readline()       # Read one line
    lines = f.readlines()     # Read all lines into list
```

### Writing
```python
with open("output.txt", "w") as f:
    f.write("Hello, World!\n")
    f.writelines(["Line 1\n", "Line 2\n"])
```

### Appending
```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```
