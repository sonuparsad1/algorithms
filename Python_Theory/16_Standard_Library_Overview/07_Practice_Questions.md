# Practice Questions - Standard Library

## Questions

### Q1: Counter Usage
Count word frequency in a text using `Counter`.

### Q2: Date Arithmetic
Calculate the number of days between two dates.

### Q3: JSON Processing
Read a JSON file and extract specific fields.

### Q4: Regular Expression
Extract all email addresses from text.

### Q5: Path Operations
List all Python files in a directory recursively.

---

## Solutions

### A1: Counter Usage
```python
from collections import Counter

text = "the quick brown fox jumps over the lazy dog the fox"
words = text.split()
word_freq = Counter(words)

print(word_freq.most_common(3))
# [('the', 3), ('fox', 2), ('quick', 1)]
```

### A2: Date Arithmetic
```python
from datetime import datetime

date1 = datetime(2024, 1, 1)
date2 = datetime(2024, 12, 31)

difference = date2 - date1
print(f"Days: {difference.days}")  # 365
```

### A3: JSON Processing
```python
import json

with open('data.json') as f:
    data = json.load(f)

# Extract names
names = [item['name'] for item in data['users']]
print(names)
```

### A4: Regular Expression
```python
import re

text = "Contact us at info@example.com or support@test.org"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(emails)
# ['info@example.com', 'support@test.org']
```

### A5: Path Operations
```python
from pathlib import Path

python_files = list(Path('.').rglob('*.py'))
for file in python_files:
    print(file)
```
