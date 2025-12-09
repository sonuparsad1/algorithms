# Real Analysis: Rigorous Foundations of Calculus

## 1. The Real Number System ($\mathbb{R}$)

Unlike floating point numbers in computers, Real Numbers ($\mathbb{R}$) are **Continuous** and **Complete**.
*   **Completeness Axiom**: Every non-empty subset of $\mathbb{R}$ that is bounded above has a **Least Upper Bound** (Supremum).
*   **Implication for CS**: Floating point arithmetic breaks these axioms (e.g., associativity errors, underflow). Understanding "Epsilon" ($\epsilon$) is crucial.

## 2. Sequences and Convergence

A sequence $(x_n)$ converges to $L$ ($\lim_{n \to \infty} x_n = L$) if:
$$ \forall \epsilon > 0, \exists N \in \mathbb{N} \text{ such that } \forall n \ge N, |x_n - L| < \epsilon $$
*   **Cauchy Sequence**: Items get closer to *each other*. In $\mathbb{R}$, Cauchy $\iff$ Convergent.
*   **Big-O Notation**: Formally defined using limits superior. $f(n) = O(g(n)) \iff \limsup |f(n)/g(n)| < \infty$.

## 3. Continuity and Limits

A function $f$ is continuous at $c$ if $\lim_{x \to c} f(x) = f(c)$.
*   **Delta-Epsilon Definition**: $\forall \epsilon > 0, \exists \delta > 0$ such that $|x - c| < \delta \implies |f(x) - f(c)| < \epsilon$.
*   **Lipschitz Continuity**: $|f(x) - f(y)| \le K |x - y|$. Stronger than uniform continuity. Critical in **GANs (Generative Adversarial Networks)** training stability (Wasserstein GAN).

## 4. Derivatives and Smoothness

Slope of the tangent line.
$$ f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} $$
*   **Differentiability classes ($C^k$)**:
    *   $C^0$: Continuous.
    *   $C^1$: Differentiable, derivative is continuous (Smooth-ish).
    *   $C^\infty$: Infinitely differentiable (Smooth).
    *   **ReLU**: Not $C^1$ at 0. But practically useful.

## 5. Taylor Series

Approximating functions with polynomials.
$$ f(x) \approx \sum_{n=0}^k \frac{f^{(n)}(a)}{n!} (x-a)^n $$
*   **CS Application**: Optimization algorithms (Newton's Method) use 2nd order Taylor approximation.

## 6. Integration (Riemann vs Lebesgue)

*   **Riemann**: Sum of rectangles. Good for continuous functions.
*   **Lebesgue**: Partitions the range. Handles weird functions (like Dirichlet function). standard necessity for Probability Theory.
