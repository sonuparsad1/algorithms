# Real Analysis: Problems and Solutions

## Problem 1: Square Root without Math Library

**Statement**: Compute `sqrt(n)` to precision `p`.
**Approach**: Newton's Method on $f(x) = x^2 - n$.
*   $f'(x) = 2x$.
*   Update: $x \leftarrow x - (x^2 - n)/(2x) = (x + n/x) / 2$.
*   This is the Babylonian Method.

**Python**:
```python
def my_sqrt(n):
    if n < 0: raise ValueError
    x = n
    while abs(x*x - n) > 1e-10:
        x = (x + n/x) / 2
    return x
```

## Problem 2: Ternary Search for Unimodal Max

**Statement**: Given a function $f(x)$ that strictly increases then strictly decreases, find peak.
**Approach**:
*   Pick two points $m1 = l + (r-l)/3$, $m2 = r - (r-l)/3$.
*   If $f(m1) < f(m2)$, peak is in $[m1, r]$.
*   Else, peak is in $[l, m2]$.
*   Converges in $O(\log n)$.

## Problem 3: Simpson's Paradox (Probability/Stats boundary)

(Actually a Stats problem, replacing with Analysis problem).

## Problem 3: Continuous Knapsack (Greedy Analysis)

**Statement**: You can cut items (continuous). Maximize value in weight $W$.
**Analysis**:
*   Sort items by density $v_i / w_i$.
*   Take whole items until $W$ full. Take fraction of last item.
*   **Proof**: Exchange argument. If you take simpler density item instead of higher, you lose total value. This relies on the "Intermediate Value" property of continuous mass.

## Problem 4: Finding Fixed Point

**Statement**: $f: [0, 1] \to [0, 1]$ is continuous. Prove $f(x)=x$ has a solution and find it.
**Analytical Proof**: Let $g(x) = f(x) - x$.
$g(0) = f(0) - 0 \ge 0$.
$g(1) = f(1) - 1 \le 0$.
By IVT, exists $c$ such that $g(c)=0 \implies f(c)=c$.
**Algo**: Bisection method on $f(x)-x$.
