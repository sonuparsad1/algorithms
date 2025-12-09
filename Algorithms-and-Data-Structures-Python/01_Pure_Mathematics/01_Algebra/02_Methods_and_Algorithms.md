# Algebra: Methods and Algorithms

## 1. Modular Exponentiation

Calculating $a^b \pmod m$ efficiently is fundamental. Brute force is $O(b)$, which is exponential in the number of bits of $b$.
**Technique**: Binary Exponentiation (Square-and-Multiply).
**Complexity**: $O(\log b)$.

## 2. Euclidean Algorithm for GCD

Finding the Greatest Common Divisor (GCD) of two numbers $a, b$.
**Recursive Step**: $\gcd(a, b) = \gcd(b, a \pmod b)$.
**Base Case**: $\gcd(a, 0) = a$.
**Complexity**: $O(\log(\min(a, b)))$. Lamé's Theorem relates this to Fibonacci numbers.

## 3. Extended Euclidean Algorithm

Finds $x, y$ such that $ax + by = \gcd(a, b)$.
Essential for finding **Modular Inverse**. If $\gcd(a, m) = 1$, then $ax \equiv 1 \pmod m$.
**Algorithm**:
Maintain quotients during the standard Euclidean algorithm and back-substitute.

## 4. Euler's Totient Function $\phi(n)$

Count of integers $1 \le k < n$ such that $\gcd(k, n) = 1$.
*   If $p$ is prime, $\phi(p) = p - 1$.
*   If $n = p_1^{e_1} \dots p_k^{e_k}$, then $\phi(n) = n \prod (1 - 1/p_i)$.
*   **Euler's Theorem**: $a^{\phi(n)} \equiv 1 \pmod n$.

## 5. Primitive Roots and Discrete Logarithm

A **primitive root** modulo $n$ is an integer $g$ such that every $a$ coprime to $n$ can be written as $g^k \pmod n$.
*   **Discrete Logarithm Problem**: Given $g, a, n$, find $k$. This is computationally hard and forms the basis of Diffie-Hellman Key Exchange.
*   **Algorithm**: Baby-step Giant-step ($O(\sqrt{n})$).

## 6. Fast Fourier Transform (FFT) for Polynomial Multiplication

Multiplying two polynomials of degree $n$:
*   Naive: $O(n^2)$.
*   FFT approach: $O(n \log n)$.
    1.  Evaluate polynomials at $2n$ points (Roots of Unity) using FFT.
    2.  Point-wise multiply values.
    3.  Interpolate back to coefficients using Inverse FFT.

## 7. Gaussian Elimination (Linear Algebra over Fields)

Solving systems of linear equations over any field (e.g., $\mathbb{F}_2$).
**Algorithm**: Row reduction to Reduced Row Echelon Form (RREF).
**Complexity**: $O(n^3)$.
**Application**: Solving XOR equations (lights out game), Berlekamp-Massey algo.
