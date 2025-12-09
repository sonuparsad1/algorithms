# Common String Errors

## 1. TypeError: Can Only Concatenate str
```python
# WRONG
age = 25
message = "I am " + age + " years old"  # TypeError

# CORRECT
message = "I am " + str(age) + " years old"
# OR
message = f"I am {age} years old"
```

## 2. IndexError: String Index Out of Range
```python
text = "Hello"
# print(text[10])  # IndexError

# CORRECT - Check length first
if len(text) > 10:
    print(text[10])
```

## 3. Immutability Error
```python
text = "Hello"
# text[0] = 'h'  # TypeError: 'str' object does not support item assignment

# CORRECT
text = 'h' + text[1:]
```

## 4. Encoding/Decoding Errors
```python
# UnicodeDecodeError when reading files
with open("file.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## 5. Strip vs Replace
```python
text = "  Hello  "

# strip() only removes from ends
print(text.strip())  # "Hello"

# replace() removes all occurrences
print(text.replace(" ", ""))  # "Hello"
```
