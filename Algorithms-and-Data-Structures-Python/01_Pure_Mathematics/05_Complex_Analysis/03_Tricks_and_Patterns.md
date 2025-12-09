# Complex Analysis: Tricks and Patterns

## 1. Roots of Unity Tricks

### 1.1 Sum of Roots
Sum of all $n$-th roots of unity is 0 (for $n > 1$).
$\sum_{k=0}^{n-1} \omega^k = \frac{\omega^n - 1}{\omega - 1} = 0$.

### 1.2 Filtering
To extract coefficients where index is multiple of $k$:
Evaluate polynomial at all $k$-th roots of unity and average.
**App**: Solving combinatorial problems with modulo constraints.

## 2. Rotation as Multiplication

To rotate a 2D point $(x, y)$ by $\theta$:
Don't use $2 \times 2$ matrices.
Use $z = x + iy$.
$z_{new} = z \cdot e^{i\theta}$.
Much cleaner code and math derivation.

## 3. Analytic Continuation

If two holomorphic functions agree on a small line segment, they agree everywhere.
**Trick**: Prove identity for real $x$, it holds for complex $z$.
Example: $\sin^2 z + \cos^2 z = 1$ is true for all $\mathbb{C}$.

## 4. Argument Principle

To count zeros of $f(z)$ inside a contour:
$$ \frac{1}{2\pi i} \oint \frac{f'(z)}{f(z)} dz = N - P $$
($N$ zeros, $P$ poles).
**App**: Nyquist Stability Criterion in Control Theory.

## 5. Identifying Circle Equation
Equation $|z - a| = r$ is a circle.
Can be expanded: $(z-a)(\bar{z}-\bar{a}) = r^2$.
$z\bar{z} - z\bar{a} - \bar{z}a + |a|^2 - r^2 = 0$.
Useful in computational geometry involving inversion.
