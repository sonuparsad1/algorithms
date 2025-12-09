# String Formatting

## 1. f-strings (Python 3.6+) - RECOMMENDED
```python
name = "Alice"
age = 30

message = f"My name is {name} and I am {age} years old"
print(message)

# Expressions inside {}
print(f"Next year I'll be {age + 1}")

# Formatting numbers
pi = 3.14159
print(f"Pi is approximately {pi:.2f}")  # 3.14
```

## 2. str.format()
```python
message = "My name is {} and I am {} years old".format("Bob", 25)

# Named placeholders
message = "My name is {name} and I am {age} years old".format(name="Bob", age=25)

# Formatting
print("{:.2f}".format(3.14159))  # 3.14
```

## 3. % Operator (Old Style)
```python
name = "Charlie"
age = 35

message = "My name is %s and I am %d years old" % (name, age)
```

## Format Specifications
```python
number = 1234.5678

print(f"{number:10}")      # '1234.5678 ' (width 10)
print(f"{number:10.2f}")   # '   1234.57' (width 10, 2 decimals)
print(f"{number:010.2f}")  # '0001234.57' (zero-padded)
print(f"{number:,}")       # '1,234.5678' (thousands separator)
```
