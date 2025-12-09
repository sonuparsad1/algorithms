# Practice Questions - File Handling

## Questions

### Q1: File Copy
Write a function to copy a file from source to destination.

### Q2: Line Counter
Count the number of lines in a text file.

### Q3: Find and Replace
Replace all occurrences of a word in a file.

### Q4: Merge Files
Merge multiple text files into one.

### Q5: CSV Filter
Filter CSV rows based on a condition.

---

## Solutions

### A1: File Copy
```python
def copy_file(source, destination):
    try:
        with open(source, "rb") as src, open(destination, "wb") as dst:
            dst.write(src.read())
        return True
    except FileNotFoundError:
        return False

copy_file("input.txt", "output.txt")
```

### A2: Line Counter
```python
def count_lines(filename):
    try:
        with open(filename, "r") as f:
            return sum(1 for line in f)
    except FileNotFoundError:
        return 0

lines = count_lines("document.txt")
print(f"Lines: {lines}")
```

### A3: Find and Replace
```python
def find_replace(filename, old, new):
    with open(filename, "r") as f:
        content = f.read()
    
    content = content.replace(old, new)
    
    with open(filename, "w") as f:
        f.write(content)

find_replace("file.txt", "old_word", "new_word")
```

### A4: Merge Files
```python
def merge_files(input_files, output_file):
    with open(output_file, "w") as outfile:
        for filename in input_files:
            with open(filename, "r") as infile:
                outfile.write(infile.read())
                outfile.write("\n")

merge_files(["file1.txt", "file2.txt"], "merged.txt")
```

### A5: CSV Filter
```python
import csv

def filter_csv(input_file, output_file, condition):
    with open(input_file, "r") as infile, open(output_file, "w", newline='') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        
        writer.writeheader()
        for row in reader:
            if condition(row):
                writer.writerow(row)

# Filter rows where age > 25
filter_csv("people.csv", "filtered.csv", lambda row: int(row["age"]) > 25)
```
