# File Handling Methods and Best Practices

## File Object Methods
```python
with open("file.txt", "r") as f:
    # Position
    pos = f.tell()        # Get current position
    f.seek(0)             # Move to beginning
    f.seek(0, 2)          # Move to end
    
    # Reading
    char = f.read(1)      # Read 1 character
    line = f.readline()   # Read one line
    
    # Iteration
    for line in f:
        print(line.strip())
```

## Context Managers for Multiple Files
```python
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())
```

## Buffering
```python
# Unbuffered
with open("file.txt", "w", buffering=0) as f:
    f.write(b"data")

# Line buffered
with open("file.txt", "w", buffering=1) as f:
    f.write("data\n")

# Custom buffer size
with open("file.txt", "w", buffering=8192) as f:
    f.write("data")
```

## File Locking (Platform-specific)
```python
import fcntl  # Unix only

with open("file.txt", "w") as f:
    fcntl.flock(f.fileno(), fcntl.LOCK_EX)  # Exclusive lock
    f.write("data")
    fcntl.flock(f.fileno(), fcntl.LOCK_UN)  # Unlock
```
