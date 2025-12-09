# Loop Control Statements (break, continue, pass)

Loop control statements change the execution from its normal sequence.

## 1. Break
Terminates the loop containing it. Control of the program flows to the statement immediately after the body of the loop.

```python
for val in "string":
    if val == "i":
        break
    print(val)
print("The end")

# Output:
# s
# t
# r
# The end
```

## 2. Continue
Skips the rest of the code inside `exclude` the current iteration only. Loop does not terminate but continues on with the next iteration.

```python
for val in "string":
    if val == "i":
        continue
    print(val)
print("The end")

# Output:
# s
# t
# r
# n
# g
# The end
```

## 3. Pass
The `pass` statement is a null operation; nothing happens when it executes. It is used as a placeholder.

```python
for x in [0, 1, 2]:
    pass # To be implemented later
```

## The `else` Clause in Loops
Python allows `else` at the end of a `for` or `while` loop.
- The `else` block executes **only if the loop completes normally**.
- It does **not** execute if the loop was stopped by a `break`.

```python
for n in range(5):
    if n == 10:
        break
else:
    print("Loop completed successfully!")
# Output: Loop completed successfully!
```
