# Abstract Algebra: Tricks and Patterns

## 1. GCD of Polynomials
Just like integers, polynomials have GCD.
**Pattern**: Use `numpy.polynomial` or implement standard Euclidean algo for polynomials over a field. Use to find common roots.

## 2. Power of Permutation
To compute $P^k$ for large $k$:
1.  Decompose $P$ into cycles.
2.  For a cycle of length $L$, the effect of $P^k$ is shifting elements by $k \pmod L$.
3.  Reconstruct the permutation.
**Complexity**: $O(N)$. Much faster than matrix exponentiation or composition ($O(N \log k)$ or $O(N)$ with composition overhead).

## 3. Order of Permutation
The smallest $k$ such that $P^k = I$.
**Trick**: $\text{Order}(P) = \text{LCM}(\text{length of cycle}_1, \dots, \text{length of cycle}_m)$.
**CP Application**: "What is the maximum order of a permutation of size $N$?" -> Landau's Function $g(n)$. Maximum LCM of partition of $n$.

## 4. Fixed Points Calculation (Burnside Shortcut)
For rotational symmetry of $N$ items with $C$ colors:
*   Rotation by $k$ units ($0 \le k < N$).
*   Number of cycles is $\gcd(k, N)$.
*   Contribution: $C^{\gcd(k, N)}$.
*   **Total**: $\frac{1}{N} \sum_{k=1}^N C^{\gcd(k, N)}$.

## 5. Conjugacy Classes
In $S_n$, two permutations are conjugate $\iff$ they have the same cycle type (same number of cycles of each length).
**Trick**: Iterate partitions of $N$ to sum over $S_n$ quickly using Polya, instead of iterating $n!$ elements.
