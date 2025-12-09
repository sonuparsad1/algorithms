# While Loops

## Definition
With the `while` loop, we can execute a set of statements as long as a condition is true.

## Syntax
```python
while condition:
    # Code block
```

**Warning**: Remember to increment/change the variable used in the condition to avoid an **infinite loop**.

## Examples

### Basic While Loop
```python
i = 1
while i < 6:
    print(i)
    i += 1  # Important: Increment i
```

## When to use `while` vs `for`?
- Use **for loops** when you know exactly how many times you want to loop (e.g., iterating over a list).
- Use **while loops** when you want to loop until a specific condition is met, and you don't know beforehand how many iterations that will take (e.g., waiting for user input).

## Infinite Loops
Sometimes infinite loops are useful (e.g., servers, game loops), but accidental ones crash programs.
```python
# Infinite loop example (Use Ctrl+C to stop)
# while True:
#     print("This will run forever")
```
