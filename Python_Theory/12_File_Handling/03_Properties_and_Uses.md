# Binary Files and Special Formats

## Binary Files
```python
# Read binary
with open("image.png", "rb") as f:
    data = f.read()

# Write binary
with open("output.bin", "wb") as f:
    f.write(bytes([0, 1, 2, 3]))
```

## CSV Files
```python
import csv

# Write CSV
with open("data.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 30])

# Read CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Using DictReader/DictWriter
with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["Name"], row["Age"])
```

## JSON Files
```python
import json

# Write JSON
data = {"name": "Alice", "age": 30}
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read JSON
with open("data.json", "r") as f:
    data = json.load(f)
```

## Pickle (Python Objects)
```python
import pickle

# Save object
data = {"key": "value", "list": [1, 2, 3]}
with open("data.pkl", "wb") as f:
    pickle.dump(data, f)

# Load object
with open("data.pkl", "rb") as f:
    data = pickle.load(f)
```
