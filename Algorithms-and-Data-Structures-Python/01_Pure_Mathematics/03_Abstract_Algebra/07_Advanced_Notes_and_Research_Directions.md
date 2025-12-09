# Abstract Algebra: Advanced Notes and Research Directions

## 1. Representation Theory

Studying groups by mapping them to Matrix Groups (GL(n)).
*   **Character Theory**: Trace of the representation matrices. Simplifies group analysis significantly (e.g., Burnside's $p^a q^b$ theorem).
*   **Application**: FFT is essentially Representation Theory of finite relationships. Non-abelian FFT uses representations of non-commutative groups.

## 2. Monster Group

The largest sporadic simple group. Order $\approx 8 \times 10^{53}$.
**Monstrous Moonshine**: Connection between the Monster Group and Modular Functions in Number Theory.

## 3. Lattice-Based Cryptography

**Lattices**: A discrete subgroup of $\mathbb{R}^n$ (like a grid).
**Shortest Vector Problem (SVP)**: Hard problem that is basis for Post-Quantum Cryptography (kyber, Dilithium).
Unlike RSA/ECC, Lattice problems are believed to be hard even for Quantum Computers.

## 4. Category Theory

The "Algebra of Algebra". Abstracts structures (objects) and mappings (morphisms).
**Haskell/Functional Programming**: Deeply connected to Category Theory (Monads, Functors).
*   A **Monad** is "just a monoid in the category of endofunctors".
