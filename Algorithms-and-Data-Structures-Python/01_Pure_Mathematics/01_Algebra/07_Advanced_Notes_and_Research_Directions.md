# Algebra: Advanced Notes and Research Directions

## 1. Abstract Algebra Deeper Dive

### 1.1 Solvable Groups and Galois Theory
*   **Galois Theory** connects Field Theory and Group Theory. It explains why there is no general formula for quintic equations (because $S_5$ is not a solvable group).
*   **Application**: Advanced error-correcting codes and lattice-based cryptography often draw on these deeper properties.

### 1.2 Ring of Polynomials
*   $F[x] / P(x)$ forms a field if $P(x)$ is irreducible.
*   **Research**: Optimizing arithmetic in $GF(2^{128})$ is crucial for GCM mode in AES.
*   **NTRU Encryption**: Operations occur in a truncated polynomial ring $R = \mathbb{Z}[X]/(X^N - 1)$.

## 2. Homomorphic Encryption
Allows computation on encrypted data without decrypting it ($E(a) + E(b) \to E(a+b)$).
*   **Partially Homomorphic**: RSA is multiplicative ($E(m_1)E(m_2) = E(m_1 m_2)$).
*   **Fully Homomorphic Encryption (FHE)**: Based on Lattice problems (LWE - Learning With Errors).

## 3. Pairing-Based Cryptography
Uses **Bilinear Maps** (Pairings) $e: G_1 \times G_2 \to G_T$.
*   $e(aP, bQ) = e(P, Q)^{ab}$.
*   Allows for **Identity-Based Encryption (IBE)** and short signatures (BLS).

## 4. Primality Testing
*   **Miller-Rabin**: Probabilistic. Standard in practice.
*   **AKS (Agrawal-Kayal-Saxena)**: Deterministic polynomial time. Theoretical breakthrough (2002).

## 5. Integer Factorization
*   **General Number Field Sieve (GNFS)**: Fastest known classical algorithm.
*   **Shor's Algorithm**: Quantum algorithm that factors in polynomial time. Threatens RSA.
