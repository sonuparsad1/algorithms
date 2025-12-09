# File Paths and Directory Operations

## Working with Paths

### Using `os.path`
```python
import os

# Join paths
path = os.path.join("folder", "subfolder", "file.txt")

# Get absolute path
abs_path = os.path.abspath("file.txt")

# Check if exists
exists = os.path.exists("file.txt")
is_file = os.path.isfile("file.txt")
is_dir = os.path.isdir("folder")

# Get file info
size = os.path.getsize("file.txt")
basename = os.path.basename("/path/to/file.txt")  # "file.txt"
dirname = os.path.dirname("/path/to/file.txt")    # "/path/to"
```

### Using `pathlib` (Modern Approach)
```python
from pathlib import Path

# Create path object
path = Path("folder") / "subfolder" / "file.txt"

# Check existence
if path.exists():
    print("File exists")

# Read/write
content = path.read_text()
path.write_text("Hello")

# Get parts
print(path.name)      # "file.txt"
print(path.stem)      # "file"
print(path.suffix)    # ".txt"
print(path.parent)    # "folder/subfolder"
```

## Directory Operations
```python
import os

# Create directory
os.mkdir("new_folder")
os.makedirs("path/to/folder", exist_ok=True)  # Create nested

# List directory
files = os.listdir(".")

# Walk directory tree
for root, dirs, files in os.walk("."):
    for file in files:
        print(os.path.join(root, file))

# Remove
os.remove("file.txt")      # Delete file
os.rmdir("folder")         # Delete empty directory
import shutil
shutil.rmtree("folder")    # Delete directory and contents
```
