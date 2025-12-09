# Practice Questions - Introduction to Python

## Beginner Level

### Q1: First Program
Write a Python program that prints your name, age, and favorite hobby on separate lines.

### Q2: Simple Math
Create a program that calculates and prints the area of a rectangle with length 10 and width 5.
Formula: `Area = length × width`

### Q3: Temperature Converter
Write a program that converts 100°F to Celsius.
Formula: `C = (F - 32) × 5/9`

### Q4: String Manipulation
Create a variable with your full name. Print:
- The length of your name
- Your name in uppercase
- Your name in lowercase

### Q5: Type Checking
Create variables of different types (int, float, str, bool) and print their types using the `type()` function.

---

## Intermediate Level

### Q6: User Input Calculator
Write a program that:
1. Asks the user for two numbers
2. Asks for an operation (+, -, *, /)
3. Performs the operation and displays the result

### Q7: List Operations
Create a list of 5 favorite movies. Write code to:
- Print the first movie
- Print the last movie
- Add a new movie to the list
- Print the total number of movies

### Q8: Even or Odd
Write a program that asks the user for a number and tells them whether it's even or odd.

### Q9: Grade Calculator
Write a program that takes a numerical score (0-100) and prints the letter grade:
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: Below 60

### Q10: Sum of Numbers
Write a program that calculates the sum of all numbers from 1 to 100.

---

## Solutions

### A1: First Program
```python
print("Name: Alice Johnson")
print("Age: 25")
print("Hobby: Photography")
```

### A2: Simple Math
```python
length = 10
width = 5
area = length * width
print(f"Area of rectangle: {area}")
```

### A3: Temperature Converter
```python
fahrenheit = 100
celsius = (fahrenheit - 32) * 5/9
print(f"{fahrenheit}°F = {celsius:.2f}°C")
```

### A4: String Manipulation
```python
name = "John Doe"
print(f"Length: {len(name)}")
print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")
```

### A5: Type Checking
```python
num_int = 42
num_float = 3.14
text = "Hello"
flag = True

print(type(num_int))    # <class 'int'>
print(type(num_float))  # <class 'float'>
print(type(text))       # <class 'str'>
print(type(flag))       # <class 'bool'>
```

### A6: User Input Calculator
```python
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid operation"

print(f"Result: {result}")
```

### A7: List Operations
```python
movies = ["Inception", "The Matrix", "Interstellar", "The Prestige", "Memento"]

print(f"First movie: {movies[0]}")
print(f"Last movie: {movies[-1]}")

movies.append("Tenet")
print(f"Total movies: {len(movies)}")
print(f"Updated list: {movies}")
```

### A8: Even or Odd
```python
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")
```

### A9: Grade Calculator
```python
score = int(input("Enter score (0-100): "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

### A10: Sum of Numbers
```python
# Method 1: Using a loop
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")

# Method 2: Using formula (more efficient)
n = 100
sum_formula = n * (n + 1) // 2
print(f"Sum: {sum_formula}")

# Method 3: Using built-in sum()
sum_builtin = sum(range(1, 101))
print(f"Sum: {sum_builtin}")
```

---

## Challenge Questions

### C1: Palindrome Checker
Write a program that checks if a word is a palindrome (reads the same forwards and backwards).
Example: "racecar" is a palindrome.

### C2: Fibonacci Sequence
Write a program that prints the first 10 numbers in the Fibonacci sequence.
(0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

### C3: Prime Number Checker
Write a program that checks if a number is prime.

---

## Challenge Solutions

### C1: Palindrome Checker
```python
word = input("Enter a word: ").lower()
if word == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")
```

### C2: Fibonacci Sequence
```python
n = 10
a, b = 0, 1
print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
```

### C3: Prime Number Checker
```python
num = int(input("Enter a number: "))

if num < 2:
    print(f"{num} is not prime")
else:
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
```
