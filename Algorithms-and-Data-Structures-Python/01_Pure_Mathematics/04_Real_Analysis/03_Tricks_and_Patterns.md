# Real Analysis: Tricks and Patterns

## 1. Handling Floating Point (The "Epsilon" Pattern)

In Python/C++, never strictly check `a == b` for floats.
**Pattern**:
```python
EPS = 1e-9
if abs(a - b) < EPS: ...
```

## 2. Log-Sum-Exp Trick

When computing $\log(\sum e^{x_i})$ (common in ML softmax), naive computation overflows if $x_i$ is large.
**Trick**:
$$ \log(\sum e^{x_i}) = \max(x) + \log(\sum e^{x_i - \max(x)}) $$
This effectively shifts exponents to be $\le 0$, preventing overflow.

## 3. Finding Roots of Monotonic Functions
If you need to invert a monotonic function $y = f(x)$ (find $x$ for given $y$):
**Pattern**: Use Binary Search on the Answer.
*   Continuous domain: Bisection usually 60-100 iterations gives high precision.
*   Discrete domain: Standard binary search.

## 4. Convexity Tricks
If $f$ is Convex ($f'' > 0$):
*   Local minimum is Global minimum.
*   **Jensen's Inequality**: $E[f(X)] \ge f(E[X])$.
*   **Ternary Search**: Use to find minimum of unimodal function in $O(\log n)$.

## 5. Kahan Summation Algorithm

Summing a large array of floats accumulates error.
**Trick**: Maintain a `c` (compensation) variable to track low-order bits lost in addition.
Reduces error from $O(N \epsilon)$ to $O(1 \epsilon)$ effectively.
