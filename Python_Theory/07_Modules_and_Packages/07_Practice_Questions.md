# Practice Questions - Modules and Packages

## Questions

### Q1: Create a Module
Create a module `calculator.py` with functions for add, subtract, multiply, and divide. Import and use it in another file.

### Q2: Package Structure
Create a package `geometry` with modules `circle.py` and `rectangle.py`, each containing area and perimeter functions.

### Q3: Import Variations
Given `import math`, write three different ways to calculate the square root of 25.

### Q4: Virtual Environment
Create a virtual environment, activate it, install `requests`, and freeze the requirements.

### Q5: Fix the Import
```python
# main.py
import utils

print(utils.greet("Alice"))
```

Create `utils.py` to make this work.

---

## Solutions

### A1: Calculator Module

**calculator.py:**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
```

**main.py:**
```python
import calculator

print(calculator.add(10, 5))       # 15
print(calculator.subtract(10, 5))  # 5
print(calculator.multiply(10, 5))  # 50
print(calculator.divide(10, 5))    # 2.0
```

### A2: Geometry Package

```
geometry/
├── __init__.py
├── circle.py
└── rectangle.py
```

**geometry/circle.py:**
```python
import math

def area(radius):
    return math.pi * radius ** 2

def perimeter(radius):
    return 2 * math.pi * radius
```

**geometry/rectangle.py:**
```python
def area(length, width):
    return length * width

def perimeter(length, width):
    return 2 * (length + width)
```

**geometry/__init__.py:**
```python
from . import circle
from . import rectangle
```

**Usage:**
```python
from geometry import circle, rectangle

print(circle.area(5))
print(rectangle.area(10, 5))
```

### A3: Import Variations

```python
import math

# Method 1
result1 = math.sqrt(25)

# Method 2
from math import sqrt
result2 = sqrt(25)

# Method 3
import math as m
result3 = m.sqrt(25)
```

### A4: Virtual Environment

```bash
# Create
python -m venv myenv

# Activate (Windows)
myenv\Scripts\activate

# Install
pip install requests

# Freeze
pip freeze > requirements.txt
```

### A5: Fix the Import

**utils.py:**
```python
def greet(name):
    return f"Hello, {name}!"
```
