# Algebra: Problems and Solutions

## Problem 1: Linear Diophantine Equation

**Statement**: Given $A, B, C$, find integer solutions for $Ax + By = C$. If no solution, print "Impossible".

**Approach**:
1.  Calculate $g = \gcd(A, B)$ using Euclidean Algo.
2.  If $C \% g \neq 0$, no integer solution exists.
3.  Use Extended Euclidean Algo to find $x_0, y_0$ such that $Ax_0 + By_0 = g$.
4.  One particular solution is $x = x_0 \cdot (C/g)$, $y = y_0 \cdot (C/g)$.
5.  General solution: $x' = x + k \cdot (B/g)$, $y' = y - k \cdot (A/g)$.

**Python Solution**:
```python
def solve_diophantine(a, b, c):
    g, x0, y0 = extended_gcd(abs(a), abs(b))
    if c % g != 0:
        return None
    
    scale = c // g
    x = x0 * scale
    y = y0 * scale
    
    # Adjust signs if a or b were negative
    if a < 0: x = -x
    if b < 0: y = -y
    return x, y
```

## Problem 2: Sum of Geometric Series Modulo M

**Statement**: Compute $S = 1 + r + r^2 + \dots + r^n \pmod m$.

**Approach**:
*   Formula: $S = \frac{r^{n+1} - 1}{r - 1}$.
*   Requires Modular Inverse of $(r-1)$. This only exists if $\gcd(r-1, m) = 1$.
*   **General Case (if inverse doesn't exist)**: Use Divide and Conquer.
    *   If $n$ is odd ($n = 2k+1$ terms? Let's say indices $0 \dots 2k$):
        $1 + \dots + r^{2k+1} = (1 + r^{k+1})(1 + r + \dots + r^k)$.
    *   If $n$ is even, reduce to odd case or handle term manually.

**Python Solution (DnC)**:
```python
def geometric_sum(r, n, m):
    # Sum r^0 + ... + r^(n-1)
    if n == 0: return 0
    if n % 2 == 0: # Even number of terms, e.g., r^0...r^3
        half_n = n // 2
        half_sum = geometric_sum(r, half_n, m)
        multiplier = (1 + pow(r, half_n, m)) % m
        return (half_sum * multiplier) % m
    else: # Odd number of terms
        return (1 + r * geometric_sum(r, n - 1, m)) % m
```

## Problem 3: Square Root Modulo P

**Statement**: Find $x$ such that $x^2 \equiv n \pmod p$.

**Approach**: Tonelli-Shanks Algorithm.
*   If $p \equiv 3 \pmod 4$, then $x \equiv \pm n^{(p+1)/4} \pmod p$.
*   For general $p$, the algorithm is more involved ($O(\log^2 p)$).

**Note**: Check Euler's Criterion first: $n^{(p-1)/2} \equiv 1 \pmod p$. If $-1$, no solution.
