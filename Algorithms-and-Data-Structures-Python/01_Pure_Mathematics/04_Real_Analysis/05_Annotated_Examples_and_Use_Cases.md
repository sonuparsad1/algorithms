# Real Analysis: Annotated Examples and Use Cases

## 1. Gradient Descent (Optimization)

**Scenario**: Training a Neural Network. Minimizing Loss $L(\theta)$.
**Methods**:
*   **Gradient Descent**: $\theta_{new} = \theta_{old} - \alpha \nabla L(\theta)$.
*   Relies on the derivative pointing in direction of steepest ascent.
*   **Lipschitz Continuity** ensures that if we take a small enough step ($\alpha < 1/L$), we strictly decrease Loss.

## 2. Audio Processing (Signals)

**Theory**: Fourier Series implies any periodic function (sound wave) can be represented as sum of infinite sines/cosines.
**Real Analysis**: Convergence of Fourier Series.
*   Phenomenon: **Gibbs Phenomenon** at discontinuities (ringing artifacts).
*   Sampling Theorem (Nyquist-Shannon): Needs rigorous limits to prove.

## 3. Zeno's Paradoxes and Infinite Series

**Problem**: Achilles and the Tortoise. To catch up, Achilles travels half distance, then half remaining... does he ever reach?
**Analysis**: The sum of an infinite Geometric Series exists and is finite.
$$ \sum_{n=1}^\infty (1/2)^n = 1 $$
This resolved centuries of philosophical debate.

## 4. Probability Density Functions (PDF)

**Scenario**: Normal Distribution.
**Area**: $\int_{-\infty}^\infty \frac{1}{\sqrt{2\pi}} e^{-x^2/2} dx = 1$.
**Improper Integrals**: Integration over infinite bounds requires Limits: $\lim_{t \to \infty} \int_{-t}^t$.

## 5. Detecting Edge Cases (Analysis helps bugs)

*   **Function**: $f(x) = 1/x$.
*   **Problem**: Not continuous at 0.
*   **Code**: `if abs(x) < 1e-9: raise ValueError`.
*   **Mathematical Insight**: The limit $\lim_{x \to 0^+} f(x) = \infty$, $\lim_{x \to 0^-} f(x) = -\infty$. Discontinuity is essential, not just a nuisance.
