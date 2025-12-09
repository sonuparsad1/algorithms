# Common Standard Library Modules

## `os` and `sys`
```python
import os
import sys

# Environment
print(os.environ.get('PATH'))
print(sys.platform)  # 'win32', 'linux', 'darwin'

# Command line arguments
print(sys.argv)

# Exit
sys.exit(0)
```

## `re` - Regular Expressions
```python
import re

# Search
match = re.search(r'\d+', 'Order 123')
if match:
    print(match.group())  # '123'

# Find all
numbers = re.findall(r'\d+', 'Order 123, Item 456')
# ['123', '456']

# Replace
text = re.sub(r'\d+', 'XXX', 'Order 123')
# 'Order XXX'
```

## `random` - Random Numbers
```python
import random

# Random float [0.0, 1.0)
random.random()

# Random integer
random.randint(1, 10)

# Random choice
random.choice(['apple', 'banana', 'cherry'])

# Shuffle
items = [1, 2, 3, 4]
random.shuffle(items)
```

## `json` - JSON Handling
```python
import json

# Serialize
data = {'name': 'Alice', 'age': 30}
json_str = json.dumps(data)

# Deserialize
data = json.loads(json_str)

# File I/O
with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data = json.load(f)
```
