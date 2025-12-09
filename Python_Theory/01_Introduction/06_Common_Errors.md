# Common Errors for Beginners

## 1. SyntaxError

### Missing Colon
```python
# WRONG
if x > 5
    print("Greater")

# CORRECT
if x > 5:
    print("Greater")
```

### Incorrect Indentation
```python
# WRONG
def greet():
print("Hello")  # IndentationError

# CORRECT
def greet():
    print("Hello")
```

### Mixing Tabs and Spaces
```python
# WRONG (invisible error - mixing tabs and spaces)
def example():
    x = 5      # 4 spaces
	y = 10     # 1 tab
    
# CORRECT - Use only spaces (4 spaces is standard)
def example():
    x = 5
    y = 10
```

## 2. NameError

### Using Undefined Variable
```python
# WRONG
print(message)  # NameError: name 'message' is not defined

# CORRECT
message = "Hello"
print(message)
```

### Typo in Variable Name
```python
# WRONG
user_name = "Alice"
print(username)  # NameError (missing underscore)

# CORRECT
user_name = "Alice"
print(user_name)
```

## 3. TypeError

### Concatenating Different Types
```python
# WRONG
age = 25
print("I am " + age + " years old")  # TypeError

# CORRECT
age = 25
print("I am " + str(age) + " years old")
# OR use f-string
print(f"I am {age} years old")
```

### Calling Non-Callable Object
```python
# WRONG
x = 5
result = x()  # TypeError: 'int' object is not callable

# CORRECT
def x():
    return 5
result = x()
```

## 4. IndexError

### Accessing Out-of-Range Index
```python
# WRONG
fruits = ["apple", "banana"]
print(fruits[2])  # IndexError: list index out of range

# CORRECT
fruits = ["apple", "banana"]
if len(fruits) > 2:
    print(fruits[2])
else:
    print("Index out of range")
```

## 5. KeyError

### Accessing Non-Existent Dictionary Key
```python
# WRONG
student = {"name": "John", "age": 20}
print(student["grade"])  # KeyError: 'grade'

# CORRECT - Use .get() method
student = {"name": "John", "age": 20}
print(student.get("grade", "Not found"))  # Returns "Not found"
```

## 6. ValueError

### Invalid Type Conversion
```python
# WRONG
age = int("twenty")  # ValueError: invalid literal for int()

# CORRECT - Validate input
age_str = input("Enter age: ")
if age_str.isdigit():
    age = int(age_str)
else:
    print("Please enter a valid number")
```

## 7. AttributeError

### Calling Non-Existent Method
```python
# WRONG
x = 5
x.append(10)  # AttributeError: 'int' object has no attribute 'append'

# CORRECT
x = [5]  # Use a list instead
x.append(10)
```

## 8. IndentationError

### Unexpected Indent
```python
# WRONG
x = 5
    y = 10  # IndentationError: unexpected indent

# CORRECT
x = 5
y = 10
```

### Unindent Does Not Match
```python
# WRONG
def example():
    if True:
        print("Hello")
      print("World")  # IndentationError

# CORRECT
def example():
    if True:
        print("Hello")
    print("World")
```

## 9. ZeroDivisionError

### Division by Zero
```python
# WRONG
result = 10 / 0  # ZeroDivisionError

# CORRECT - Check before dividing
divisor = 0
if divisor != 0:
    result = 10 / divisor
else:
    print("Cannot divide by zero")
```

## 10. ImportError / ModuleNotFoundError

### Importing Non-Existent Module
```python
# WRONG
import nonexistent_module  # ModuleNotFoundError

# CORRECT - Install the module first
# pip install module_name
import numpy  # After installing: pip install numpy
```

## Tips to Avoid Errors

1. **Read Error Messages Carefully**: Python error messages tell you exactly what went wrong and where.
2. **Use an IDE**: IDEs like PyCharm, VS Code highlight syntax errors before you run the code.
3. **Print Debugging**: Use `print()` statements to check variable values.
4. **Use Try-Except**: Handle potential errors gracefully.
   ```python
   try:
       age = int(input("Enter age: "))
   except ValueError:
       print("Invalid input. Please enter a number.")
   ```
5. **Follow PEP 8**: Python's style guide helps maintain consistent, readable code.
