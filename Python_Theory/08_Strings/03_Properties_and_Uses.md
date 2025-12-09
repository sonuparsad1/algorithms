# String Methods

## Case Conversion
```python
text = "Hello World"

print(text.upper())       # "HELLO WORLD"
print(text.lower())       # "hello world"
print(text.capitalize())  # "Hello world"
print(text.title())       # "Hello World"
print(text.swapcase())    # "hELLO wORLD"
```

## Searching
```python
text = "Python Programming"

print(text.find("Pro"))      # 7 (index of first occurrence)
print(text.find("Java"))     # -1 (not found)
print(text.index("Pro"))     # 7 (raises ValueError if not found)
print(text.count("m"))       # 2
print(text.startswith("Py")) # True
print(text.endswith("ing"))  # True
```

## Modification
```python
text = "  Hello World  "

print(text.strip())        # "Hello World" (remove whitespace)
print(text.lstrip())       # "Hello World  "
print(text.rstrip())       # "  Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "
```

## Splitting and Joining
```python
text = "apple,banana,cherry"

# Split
fruits = text.split(",")  # ['apple', 'banana', 'cherry']

# Join
result = " - ".join(fruits)  # "apple - banana - cherry"
```

## Checking
```python
print("123".isdigit())     # True
print("abc".isalpha())     # True
print("abc123".isalnum())  # True
print("   ".isspace())     # True
```
