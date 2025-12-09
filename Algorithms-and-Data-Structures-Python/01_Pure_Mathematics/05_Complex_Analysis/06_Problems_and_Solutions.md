# Complex Analysis: Problems and Solutions

## Problem 1: Integration via Residues

**Statement**: Evaluate $I = \int_{-\infty}^\infty \frac{1}{x^2 + 1} dx$.
**Real Method**: $\arctan(x)|_{-\infty}^\infty = \pi/2 - (-\pi/2) = \pi$.
**Complex Method**:
1.  Consider $f(z) = \frac{1}{z^2 + 1}$. Singularities at $z = \pm i$.
2.  Contour: Semi-circle in upper half plane $R \to \infty$.
3.  Residue at $z=i$: $\lim_{z \to i} (z-i) \frac{1}{(z-i)(z+i)} = \frac{1}{2i}$.
4.  Integral = $2\pi i \times \text{Res} = 2\pi i (1/2i) = \pi$. Matches.

## Problem 2: Counting Roots (Rouche's Theorem)

**Statement**: How many roots does $z^5 + 3z + 1 = 0$ have inside $|z| < 1$?
**Theorem**: If $|g(z)| < |f(z)|$ on boundary, $f$ and $f+g$ have same number of zeros.
**Attempt**:
*   Let $f(z) = 3z$, $g(z) = z^5 + 1$.
*   On boundary $|z|=1$: $|f(z)| = 3$. $|g(z)| \le |z|^5 + 1 = 2$.
*   Since $2 < 3$, $|g| < |f|$.
*   $f(z)=3z$ has 1 zero inside.
*   Therefore, $z^5 + 3z + 1$ has **1 zero** inside.

## Problem 3: Conformal Map Construction

**Statement**: Map Upper Half Plane ($\text{Im}(z) > 0$) to Unit Disk ($|w| < 1$).
**Ansatz**: Möbius transform.
*   Map $i \to 0$ (Center).
*   Map $0 \to -1$ (Boundary).
*   Map $\infty \to 1$ (Boundary).
**Result**: $f(z) = \frac{z-i}{z+i}$.
*   This is the **Cayley Transform**.
