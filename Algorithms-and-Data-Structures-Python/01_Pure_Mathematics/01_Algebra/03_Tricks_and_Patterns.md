# Algebra: Tricks and Patterns (Competitive Programming & Optimization)

## 1. Modular Arithmetic Patterns

### 1.1 Negative Modulo
In Python, `-5 % 3` is `1`. In C++/Java, it might be `-2`.
**Pattern**: Always normalize: `res = (a % m + m) % m`.

### 1.2 Identifying "Cycle Finding" Problems
Any sequence defined by $x_{i+1} = f(x_i) \pmod m$ will eventually cycle.
**Trick**: Use Floyd's Cycle Finding (Tortoise and Hare) to detect period $\lambda$ and pre-period $\mu$.
**App**: Pollard's Rho Algorithm for integer factorization.

### 1.3 Fermat's Little Theorem for Division
To compute $(a / b) \pmod p$ where $p$ is prime:
Compute $a \cdot b^{p-2} \pmod p$.
**Precondition**: $b$ is not a multiple of $p$.

## 2. Combinatorics and Modulo

### 2.1 Precomputing Factorials
To calculate $\binom{n}{k} \pmod p$ repeatedly:
1.  Precompute fact $[i] = i! \pmod p$.
2.  Precompute invFact $[i] = (i!)^{-1} \pmod p$ using Fermat's Little Theorem (one exp call, then build backwards: $1/((n-1)!) = (1/n!) \cdot n$).

### 2.2 Lucas Theorem
For huge $n, k$ and small prime $p$, $\binom{n}{k} \equiv \prod \binom{n_i}{k_i} \pmod p$, where $n_i, k_i$ are digits in base $p$.

## 3. Matrix Exponentiation (Algebra + DP)
Linear recurrence relations (Fibonacci, Tilings) can be solved in $O(k^3 \log n)$ using matrix exponentiation.
**Pattern**:
State vector $V_i$. Transition $V_{i+1} = M \times V_i$.
Result: $V_n = M^n \times V_0$.

## 4. GCD Properties
*   $\gcd(a, b, c) = \gcd(a, \gcd(b, c))$.
*   $\gcd(a, b) = \gcd(a, b-a)$.
*   **Optimization**: $\gcd(a, b)$ is very fast. Don't hesitate to use it in inner loops if values decrease rapidly.

## 5. Identifying Groups in Disguise
*   **XOR Operations**: Determine a vector space over $\mathbb{F}_2$. Use Gaussian Elimination / Linear Basis to find max XOR subset, etc.
*   **Permutations**: Decompose into disjoint cycles. Order of permutation = LCM of cycle lengths.
