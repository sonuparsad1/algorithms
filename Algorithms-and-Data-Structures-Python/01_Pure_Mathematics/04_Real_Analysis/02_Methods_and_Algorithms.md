# Real Analysis: Methods and Algorithms

## 1. Root Finding (Solving $f(x) = 0$)

### 1.1 Bisection Method
**Theory**: Intermediate Value Theorem. If $f(a)$ and $f(b)$ have opposite signs, a root exists in $[a, b]$.
**Algo**: Check mid. Recurse.
**Complexity**: Linear choice of accuracy ($O(\log(1/\epsilon))$).

### 1.2 Newton-Raphson Method
**Theory**: Linear approximation using derivative.
**Algo**: $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$.
**Convergence**: Quadratic (doubles digits of precision per step) if close to root.

## 2. Numerical Differentiation

How to calculate $f'(x)$ if we only have $f$ as a black box?
*   **Finite Difference**:
    *   Forward: $\frac{f(x+h) - f(x)}{h}$. Error $O(h)$.
    *   Central: $\frac{f(x+h) - f(x-h)}{2h}$. Error $O(h^2)$. (Much Better).
*   **Automatic Differentiation (Autodiff)**: The heart of PyTorch/TensorFlow. Applies Chain Rule exactly to computer programs. NOT numerical differentiation.

## 3. Numerical Integration (Quadrature)

Calculating $\int_a^b f(x) dx$.
*   **Trapezoidal Rule**: Connect points with lines. Error $O(h^2)$.
*   **Simpson's Rule**: Connect with parabolas. Error $O(h^4)$.
*   **Monte Carlo Integration**: Sample random points. $\frac{1}{N} \sum f(x_i)$. Error $O(1/\sqrt{N})$. Good for high dimensions.

## 4. Fixed Point Iteration

Solving $x = g(x)$.
**Banach Fixed Point Theorem**: If $g$ is a contraction mapping (Lipschitz constant $K < 1$), then $x_{n+1} = g(x_n)$ converges to unique fixed point.
**App**: PageRank, iterative linear solvers.

## 5. Golden Section Search

Finding min/max of unimodal function without derivatives.
Maintains a bracket $[a, b]$ and two inner points $c, d$.
Ratio $(b-a)/(d-a)$ is the Golden Ratio $\phi$.
