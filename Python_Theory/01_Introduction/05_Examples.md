# Python Code Examples

## Example 1: Hello World
The traditional first program.

```python
print("Hello, World!")
```

**Output:**
```
Hello, World!
```

## Example 2: Variables and Types

```python
# Integer
age = 25

# Float
price = 19.99

# String
name = "Alice"

# Boolean
is_student = True

# Display types
print(type(age))        # <class 'int'>
print(type(price))      # <class 'float'>
print(type(name))       # <class 'str'>
print(type(is_student)) # <class 'bool'>
```

## Example 3: User Input and Output

```python
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Convert age to integer
age = int(age)

# Display personalized message
print(f"Hello {name}, you are {age} years old.")

# Calculate birth year (assuming current year is 2025)
birth_year = 2025 - age
print(f"You were born in approximately {birth_year}.")
```

## Example 4: Simple Calculator

```python
# Get two numbers from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

# Display results
print(f"{num1} + {num2} = {addition}")
print(f"{num1} - {num2} = {subtraction}")
print(f"{num1} * {num2} = {multiplication}")
print(f"{num1} / {num2} = {division}")
```

## Example 5: Conditional Logic

```python
# Check if number is positive, negative, or zero
number = float(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
```

## Example 6: Simple Loop

```python
# Print numbers 1 to 10
for i in range(1, 11):
    print(i, end=" ")
print()  # New line

# Print even numbers from 0 to 20
for i in range(0, 21, 2):
    print(i, end=" ")
```

**Output:**
```
1 2 3 4 5 6 7 8 9 10 
0 2 4 6 8 10 12 14 16 18 20
```

## Example 7: List Operations

```python
# Create a list
fruits = ["apple", "banana", "cherry"]

# Add an item
fruits.append("orange")

# Access items
print(fruits[0])  # apple
print(fruits[-1]) # orange (last item)

# Loop through list
for fruit in fruits:
    print(f"I like {fruit}")

# List length
print(f"Total fruits: {len(fruits)}")
```

## Example 8: Simple Function

```python
def greet(name, greeting="Hello"):
    """
    Greets a person with a custom or default greeting.
    
    Args:
        name (str): The person's name
        greeting (str): The greeting message (default: "Hello")
    
    Returns:
        str: The complete greeting message
    """
    message = f"{greeting}, {name}!"
    return message

# Call the function
print(greet("Alice"))                    # Hello, Alice!
print(greet("Bob", "Good morning"))      # Good morning, Bob!
```

## Example 9: Dictionary Usage

```python
# Create a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Access values
print(f"Name: {student['name']}")
print(f"GPA: {student['gpa']}")

# Add new key-value pair
student["year"] = "Junior"

# Loop through dictionary
for key, value in student.items():
    print(f"{key}: {value}")
```

## Example 10: File Operations

```python
# Write to a file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a test file.\n")
    file.write("Python makes file handling easy!\n")

# Read from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("sample.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline characters
```
