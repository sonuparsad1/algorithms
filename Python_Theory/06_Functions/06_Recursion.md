# Recursion

## Definition
**Recursion** is a common mathematical and programming concept. It means that a function **calls itself**.

## Theory
- **Base Case**: The condition that stops the recursion. Without it, the function calls itself forever (Stack Overflow).
- **Recursive Case**: The part where the function calls itself with a modified parameter, moving towards the base case.

## Example: Factorial
Factorial of n (`n!`) is `n * (n-1) * ... * 1`.
`5! = 5 * 4 * 3 * 2 * 1 = 120`.

```python
def factorial(n):
    # Base Case
    if n == 1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n - 1)

print(factorial(5)) # 120
```

## Analysis of Execution
`factorial(5)` calls `5 * factorial(4)`
    `factorial(4)` calls `4 * factorial(3)`
        `factorial(3)` calls `3 * factorial(2)`
            `factorial(2)` calls `2 * factorial(1)`
                `factorial(1)` returns `1`

## Pros and Cons
- **Pros**: Code looks clean and elegant for problems like tree traversals, sorting (Merge Sort, Quick Sort).
- **Cons**: Can be memory-intensive (maintains a stack frame for each call). Python has a recursion limit (usually 1000).

## Common Errors
- **RecursionError: maximum recursion depth exceeded**: Happens when there is no base case or the base case is unreachable.
