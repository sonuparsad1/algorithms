# File Handling Examples

## Example 1: Log File Analyzer
```python
def analyze_log(filename):
    error_count = 0
    warning_count = 0
    
    with open(filename, "r") as f:
        for line in f:
            if "ERROR" in line:
                error_count += 1
            elif "WARNING" in line:
                warning_count += 1
    
    return {"errors": error_count, "warnings": warning_count}

stats = analyze_log("app.log")
print(f"Errors: {stats['errors']}, Warnings: {stats['warnings']}")
```

## Example 2: CSV to JSON Converter
```python
import csv
import json

def csv_to_json(csv_file, json_file):
    data = []
    
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    
    with open(json_file, "w") as f:
        json.dump(data, f, indent=2)

csv_to_json("data.csv", "data.json")
```

## Example 3: File Backup
```python
import shutil
from datetime import datetime

def backup_file(filename):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{filename}.backup_{timestamp}"
    shutil.copy2(filename, backup_name)
    return backup_name

backup = backup_file("important.txt")
```

## Example 4: Word Frequency Counter
```python
from collections import Counter

def word_frequency(filename):
    with open(filename, "r") as f:
        words = f.read().lower().split()
    
    return Counter(words).most_common(10)

top_words = word_frequency("document.txt")
for word, count in top_words:
    print(f"{word}: {count}")
```
