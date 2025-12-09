# Linear Algebra: Advanced Notes and Research Directions

## 1. Randomized Linear Algebra

Standard matrix algorithms ($O(N^3)$) are too slow for Big Data ($N=10^6$).
**Research methods**:
*   **Sketching**: Project vectors into lower dimensions using random matrices (Johnson-Lindenstrauss Lemma) while preserving norms.
*   **Randomized SVD**: Identify range of $A$ using random vectors, then SVD on smaller subspace. Very fast approximate PCA.

## 2. Sparse Linear Algebra

Algorithms optimized for matrices where most entries are zero.
*   **Storage**: CSR (Compressed Sparse Row), CSC.
*   **Solvers**: Krylov Subspace Methods (Conjugate Gradient, GMRES). These solve $Ax=b$ by iteratively building a basis for $\{b, Ab, A^2b \dots\}$. $O(k \cdot E)$ where $E$ is edges, much faster than $N^3$.

## 3. Tensor Algebra (Multilinear Algebra)

Generalizing matrices (2D) to Tensors (nD).
*   **Tensor Decomposition**: CP (Canonical Polyadic), Tucker.
*   **Applications**: Deep Learning (PyTorch/TensorFlow are tensor algebra libraries), Chemometrics.

## 4. Quantum Linear Algebra

HHL Algorithm (Harrow-Hassidim-Lloyd).
*   Solves $Ax=b$ in $O(\log N)$ on a quantum computer (under specific conditions).
*   Offers exponential speedup over classical algorithms.

## 5. Spectral Graph Theory

Studying graphs via eigenvalues of their matrices (Adjacency, Laplacian).
*   **Cheeger's Inequality**: Relates "conductance" (bottlenecks) of a graph to the second smallest eigenvalue of Laplacian ($\lambda_2$).
*   **Graph Isomorphism**: Using spectrum to check isomorphism (imperfect but useful).
