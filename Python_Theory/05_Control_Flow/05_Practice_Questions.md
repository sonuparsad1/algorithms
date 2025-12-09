# Practice Questions - Control Flow

## Questions

### Q1: Grading System
Write a program that takes a score (0-100) and prints:
- "A" if score > 90
- "B" if score > 80
- "C" if score > 70
- "Fail" otherwise.

### Q2: Sum of Numbers
Write a `for` loop to calculate the sum of all numbers from 1 to 100.

### Q3: Pattern Printing
Use nested loops to print the following pattern:
```
*
**
***
****
*****
```

### Q4: Finder
Write a loop that searches for the number `5` in the list `[1, 9, 3, 5, 7]`. If found, print "Found!" and stop the loop.

---

## Solutions

**A1:**
```python
score = 85
if score > 90:
    print("A")
elif score > 80:
    print("B")
elif score > 70:
    print("C")
else:
    print("Fail")
```

**A2:**
```python
total = 0
for i in range(1, 101):
    total += i
print(total) # 5050
```

**A3:**
```python
for i in range(1, 6):
    print("*" * i)
# OR nested loop way:
# for i in range(1, 6):
#    for j in range(i):
#        print("*", end="")
#    print()
```

**A4:**
```python
nums = [1, 9, 3, 5, 7]
for n in nums:
    if n == 5:
        print("Found!")
        break
```
