# Algebra: Theory and Foundations

## 1. Algebraic Structures

Algebra in computer science is not just about solving equations; it's about understanding **structures** and **operations** that follow specific rules. These structures are the foundation of cryptography, coding theory, and advanced algorithm design (e.g., FFT).

### 1.1 Groups, Rings, and Fields

The hierarchy of algebraic structures defines what operations are permissible and what properties they guarantee.

#### 1.1.1 Groups
A **Group** $(G, \cdot)$ is a set $G$ equipped with a binary operation $\cdot$ satisfying:
1.  **Closure**: $\forall a, b \in G, a \cdot b \in G$.
2.  **Associativity**: $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.
3.  **Identity**: $\exists e \in G$ such that $a \cdot e = e \cdot a = a$.
4.  **Inverse**: $\forall a \in G, \exists a^{-1} \in G$ such that $a \cdot a^{-1} = a^{-1} \cdot a = e$.

*   **Abelian Group**: If $a \cdot b = b \cdot a$ (Commutativity).
*   *Examples*: Integers under addition $(\mathbb{Z}, +)$, Non-zero reals under multiplication $(\mathbb{R}^*, \cdot)$.

#### 1.1.2 Rings
A **Ring** $(R, +, \cdot)$ has two operations:
1.  $(R, +)$ is an Abelian Group.
2.  $(R, \cdot)$ is a Monoid (Closure, Associativity, Identity).
3.  **Distributivity**: $a \cdot (b + c) = a \cdot b + a \cdot c$.

*   *Example*: Integers $(\mathbb{Z}, +, \cdot)$.

#### 1.1.3 Fields
A **Field** $(F, +, \cdot)$ is a Ring where:
1.  $(F^*, \cdot)$ is an Abelian Group (Multiplicative inverses exist for all non-zero elements).
2.  Commutativity of multiplication holds.

*   *Examples*: Real numbers $\mathbb{R}$, Complex numbers $\mathbb{C}$, Finite fields $\mathbb{F}_p$ (integers modulo a prime $p$).

### 1.2 Modular Arithmetic (The Integers Modulo $n$)

The set $\mathbb{Z}_n = \{0, 1, \dots, n-1\}$ under addition and multiplication modulo $n$.
*   $\mathbb{Z}_n$ is always a Ring.
*   $\mathbb{Z}_n$ is a **Field** if and only if $n$ is **prime**.

#### Properties:
*   $a \equiv b \pmod n \iff n \mid (a - b)$.
*   $(a + b) \pmod n = ((a \pmod n) + (b \pmod n)) \pmod n$.
*   $(a \cdot b) \pmod n = ((a \pmod n) \cdot (b \pmod n)) \pmod n$.

## 2. Homomorphisms and Isomorphisms

Map functions that preserve structure. Let $(G, \cdot)$ and $(H, *)$ be groups. A function $f: G \to H$ is a **homomorphism** if:
$$ f(a \cdot b) = f(a) * f(b) $$

*   **Isomorphism**: A bijective homomorphism. If exists, $G$ and $H$ are effectively the same structure.

## 3. Polynomial Arithmetic

Polynomials over a field $F$, denoted $F[x]$, behave similarly to integers.
*   **Division Algorithm**: $A(x) = Q(x)B(x) + R(x)$, where $\deg(R) < \deg(B)$.
*   **Irreducible Polynomials**: Analogous to prime numbers.
*   **Galois Fields $GF(p^n)$**: Constructed using irreducible polynomials over $\mathbb{F}_p$. Critical for AES encryption and Reed-Solomon codes.

## 4. Theory Recommendation for CS

Understanding **Finite Fields** and **Group Theory** is non-negotiable for:
1.  **Cryptography**: RSA uses $\mathbb{Z}_n^*$, Elliptic Curve Cryptography uses groups over finite fields.
2.  **Hashing**: Cyclic Redundancy Checks (CRC) use polynomial rings.
3.  **Error Correction**: Reed-Solomon codes rely on field arithmetic.
4.  **FFT**: Fast Fourier Transform relies on roots of unity in a field (Complex or Finite).
