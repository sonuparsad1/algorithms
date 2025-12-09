# Importing Modules

## Basic Import Syntax

### 1. Import Entire Module
```python
import math

print(math.sqrt(16))  # 4.0
print(math.pi)        # 3.141592653589793
```

### 2. Import with Alias
```python
import numpy as np

arr = np.array([1, 2, 3])
```

### 3. Import Specific Items
```python
from math import sqrt, pi

print(sqrt(16))  # 4.0
print(pi)        # 3.141592653589793
```

### 4. Import All (Not Recommended)
```python
from math import *

# Can use all functions directly
print(sqrt(25))  # 5.0
```
**Warning**: Pollutes namespace, can cause conflicts.

## The `import` Statement Mechanics

When you `import mymodule`:
1. Python searches for `mymodule.py` in:
   - Current directory
   - `PYTHONPATH` environment variable directories
   - Standard library directories
2. Compiles to bytecode (`.pyc` file in `__pycache__`)
3. Executes the module code
4. Creates a module object in memory

## The `sys.path` List
```python
import sys
print(sys.path)
```
Shows all directories Python searches for modules.

## Relative vs Absolute Imports

### Absolute Import
```python
from package.subpackage import module
```

### Relative Import (within packages)
```python
from . import sibling_module        # Same directory
from .. import parent_module        # Parent directory
from ..sibling_package import mod   # Sibling package
```

## Circular Import Problem

**Problem:**
```python
# file_a.py
import file_b
def func_a():
    file_b.func_b()

# file_b.py
import file_a
def func_b():
    file_a.func_a()
```

**Solution**: Restructure code or use local imports.

## Lazy Importing
Import inside functions to delay loading:
```python
def process_data():
    import pandas as pd  # Only loaded when function is called
    df = pd.DataFrame()
```
