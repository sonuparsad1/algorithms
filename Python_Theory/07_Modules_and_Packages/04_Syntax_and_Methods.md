# Creating Packages

## Package Structure

```
mypackage/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py
```

## The `__init__.py` File

Makes a directory a package. Can be empty or contain initialization code.

**mypackage/__init__.py**
```python
"""
My custom package.
"""

# Import commonly used items to package level
from .module1 import func1
from .module2 import func2

__version__ = "1.0.0"
__all__ = ['func1', 'func2']  # Controls `from mypackage import *`
```

## Importing from Packages

```python
# Import module
import mypackage.module1

# Import specific function
from mypackage.module1 import func1

# Import from subpackage
from mypackage.subpackage import module3
```

## Namespace Packages (PEP 420)

Python 3.3+ allows packages without `__init__.py`:
```
mypackage/
├── module1.py
└── module2.py
```

Still works, but no package-level initialization.

## `__all__` Variable

Controls what gets imported with `from package import *`:

```python
# __init__.py
__all__ = ['module1', 'module2']  # Only these are imported with *
```
