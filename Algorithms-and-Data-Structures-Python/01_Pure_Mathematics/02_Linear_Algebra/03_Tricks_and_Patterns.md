# Linear Algebra: Tricks and Patterns

## 1. Matrix Exponentiation Tricks

### 1.1 Augmenting the State
Sometimes the recurrence depends on $n$ or a sum.
*   $f_n = f_{n-1} + f_{n-2} + n$.
*   State: $[f_n, f_{n-1}, n, 1]^T$.
*   Transition incorporates the $+1$ for $n$ and the $+n$ for $f_n$.

### 1.2 Graph Adjacency Matrix
*   Let $A$ be the adjacency matrix of an unweighted graph.
*   $(A^k)_{ij}$ = Number of walks of length exactly $k$ from $i$ to $j$.
*   **Trick**: If nodes are small ($N \le 50$) and $k$ is huge, use Matrix Exp.

## 2. XOR Basis (The "Linear Algebra of Bits")

To check if a number $X$ is representable by XOR sum of array $A$:
1.  Insert all $a \in A$ into a linear basis.
2.  Try to reduce $X$ using the basis.
3.  If $X$ reduces to 0, it is representable.
4.  **Max XOR**: Greedily XOR with basis elements starting from most significant bit.

## 3. Coordinate Compression

In geometry or 2D grid problems with huge coordinates but few points:
*   Map unique sorted $x$-coordinates to $0, 1, 2, \dots$.
*   Preserves relative order.
*   Transforms $10^9$ grid to $O(N)$ grid.

## 4. Vandermonde Matrix Properties

Determinant of Vandermonde matrix (geometric progression rows) has a closed form: $\prod_{1 \le i < j \le n} (x_j - x_i)$.
*   Useful in interpolation and secret sharing problems.

## 5. Cayley-Hamilton Theorem

Every square matrix satisfies its own characteristic equation: $p(A) = 0$.
*   **Trick**: Enables computing $A^{-1}$ as a polynomial in $A$ of degree $n-1$.
*   $A^n = c_{n-1}A^{n-1} + \dots + c_0 I$. Can reduce high powers of $A$ without full multiplication if we only need specific projections.

## 6. Rotation Matrices

To rotate a point $(x, y)$ by $\theta$ counter-clockwise:
$$
\begin{bmatrix} x' \\ y' \end{bmatrix} =
\begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
\begin{bmatrix} x \\ y \end{bmatrix}
$$
**Trick**: For $90^\circ$, swap and negate: $(x, y) \to (-y, x)$.

## 7. Fast Hadamard Transform (FHT)

Like FFT but for XOR convolution.
$(A * B)[k] = \sum_{i \oplus j = k} A[i] B[j]$.
Uses the Hadamard matrix structure. Complexity $O(N \log N)$.
