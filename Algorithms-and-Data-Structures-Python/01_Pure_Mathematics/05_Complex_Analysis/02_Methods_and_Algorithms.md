# Complex Analysis: Methods and Algorithms

## 1. Fast Fourier Transform (FFT)

The most important algorithm in history ($O(N \log N)$).
**Theory**: Evaluating a polynomial $P(x)$ at $n$-th Roots of Unity.
**Divide and Conquer**:
$P(x) = P_{even}(x^2) + x P_{odd}(x^2)$.
Using $\omega_n^k$, we exploit symmetry $\omega_n^{k + n/2} = -\omega_n^k$.

## 2. Möbius Transformations

Bijective maps from extended complex plane to itself.
$$ f(z) = \frac{az + b}{cz + d} $$
*   Maps circles/lines to circles/lines.
*   Used in **Image Processing** for warping.

## 3. Contour Integration (for Real Integrals)

Technique to solve hard real integrals $\int_{-\infty}^\infty f(x) dx$ by "completing the contour" in the complex plane and summing Residues.
**Method**:
1.  Choose semi-circle contour.
2.  Show integral on arc $\to 0$ as $R \to \infty$ (Jordan's Lemma).
3.  Answer is $2\pi i \sum \text{Residues}$.

## 4. Generating Fractal Images (Mandelbrot)

Iterating $z_{n+1} = z_n^2 + c$.
*   **Mandelbrot Set**: $c$ such that $|z_n|$ remains bounded starting $z_0 = 0$.
*   **Julia Sets**: Fixed $c$, vary $z_0$.

## 5. Phase Unwrapping

In signal processing, we compute phase $\phi(t) = \text{arg}(z(t))$.
This value jumps by $2\pi$.
**Algorithm**: Detect jumps $>\pi$ and add $\pm 2\pi$ to make phase continuous.
Essential for Radar/Sonar processing.
