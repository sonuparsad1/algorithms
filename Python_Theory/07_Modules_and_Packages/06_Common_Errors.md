# Common Module Errors

## 1. ModuleNotFoundError

**Error:**
```python
import nonexistent_module
# ModuleNotFoundError: No module named 'nonexistent_module'
```

**Solutions:**
- Install the package: `pip install module_name`
- Check spelling
- Ensure module is in `sys.path`

## 2. ImportError

**Error:**
```python
from math import nonexistent_function
# ImportError: cannot import name 'nonexistent_function'
```

**Solution:** Check the module's documentation for correct names.

## 3. Circular Import

**file_a.py:**
```python
import file_b
def func_a():
    return file_b.func_b()
```

**file_b.py:**
```python
import file_a
def func_b():
    return file_a.func_a()
```

**Error:** Infinite loop or `AttributeError`

**Solutions:**
- Restructure code to remove circular dependency
- Use local imports (import inside function)
- Use `import` instead of `from ... import`

## 4. Name Conflicts

```python
from math import *
from numpy import *

# Which sqrt() is being used? Namespace pollution!
result = sqrt(16)
```

**Solution:** Use explicit imports or aliases.

## 5. Relative Import in Non-Package

**Error:**
```python
from . import module  # ValueError: attempted relative import in non-package
```

**Solution:** Ensure you're inside a package (directory with `__init__.py`).

## 6. Module Caching

Python caches imported modules. Changes to a module won't reflect until restart.

**Solution:**
```python
import importlib
importlib.reload(mymodule)
```
