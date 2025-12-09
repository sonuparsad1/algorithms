# Complex Analysis: The Geometry of Numbers

## 1. Complex Numbers $\mathbb{C}$

Extensions of reals with $i^2 = -1$.
*   **Form**: $z = x + iy$.
*   **Polar Form**: $z = r e^{i\theta} = r (\cos \theta + i \sin \theta)$.
*   **Euler's Formula**: $e^{i\pi} + 1 = 0$.

### 1.1 Geometry
*   Addition: Vector addition in 2D plane.
*   Multiplication: Scale lengths ($r_1 r_2$), Add angles ($\theta_1 + \theta_2$).
*   **Roots of Unity**: Solutions to $z^n = 1$. Form a regular $n$-gon. Critical for FFT.

## 2. Holomorphic Functions

Complex differentiable functions. This is a MUCh stronger condition than real differentiability.
$$ f'(z_0) = \lim_{z \to z_0} \frac{f(z) - f(z_0)}{z - z_0} $$
Limit must be independent of direction of approach.

### 2.1 Cauchy-Riemann Equations
For $f(z) = u(x, y) + i v(x, y)$ to be holomorphic:
$$ \frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x} $$
Consequence: Holomorphic functions are $C^\infty$ (infinitely differentiable) and **Analytic** (equal to their Taylor series).

## 3. Cauchy's Integral Theorem

If $f$ is holomorphic on a simply connected domain and $\gamma$ is a closed loop:
$$ \oint_\gamma f(z) dz = 0 $$
**Path Independence**: Integration between two points is independent of path.

### 3.1 Cauchy's Integral Formula
Value inside a loop is determined by values on boundary:
$$ f(a) = \frac{1}{2\pi i} \oint_\gamma \frac{f(z)}{z-a} dz $$

## 4. Residue Theorem

A powerful tool to evaluate integrals.
$$ \oint_\gamma f(z) dz = 2\pi i \sum \text{Res}(f, a_k) $$
where $a_k$ are singularities inside $\gamma$.
*   **Residue**: The coefficient $c_{-1}$ in the Laurent Series $\sum c_n (z-a)^n$.

## 5. Conformal Mapping

Holomorphic functions preserve angles (conformal).
*   **Riemann Mapping Theorem**: Any simply connected non-empty open subset of $\mathbb{C}$ (not whole $\mathbb{C}$) can be mapped bijectively to the open unit disk.
*   **App**: Solving fluid flow (aerodynamics) on complex shapes by mapping shape to a circle.
