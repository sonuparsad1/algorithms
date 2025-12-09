# Linear Algebra: Theory and Foundations

## 1. Vector Spaces and Subspaces

The central object of linear algebra is the **Vector Space** $V$ over a field $F$.
Vectors obey addition and scalar multiplication.

### 1.1 Basis and Dimension
*   **Linear Independence**: A set $\{v_1, \dots, v_k\}$ is linearly independent if $c_1 v_1 + \dots + c_k v_k = 0 \implies c_i = 0$.
*   **Span**: The set of all linear combinations of vectors.
*   **Basis**: A linearly independent set that spans $V$.
*   **Dimension**: The size of the basis (invariant).

### 1.2 Subspaces
A subset $W \subseteq V$ is a subspace if it is closed under addition and scalar multiplication.
*   **Null Space (Kernel)** of Matrix $A$: $\{x \mid Ax = 0\}$.
*   **Column Space (Image)** of Matrix $A$: Span of columns of $A$.
*   **Rank-Nullity Theorem**: $\text{rank}(A) + \text{nullity}(A) = n$ (number of cols).

## 2. Matrices and Linear Transformations

Matrices represent linear maps between vector spaces.
If $T: \mathbb{R}^n \to \mathbb{R}^m$, there exists an $m \times n$ matrix $A$ such that $T(x) = Ax$.

### 2.1 Determinant
A scalar value $\det(A)$ characterizing square matrices.
*   Geometric interpretation: Scaling factor of volume.
*   $\det(A) \neq 0 \iff A$ is invertible.
*   Multiplicative: $\det(AB) = \det(A)\det(B)$.

### 2.2 Eigenvalues and Eigenvectors
For a square matrix $A$, if $Av = \lambda v$ ($v \neq 0$), then $\lambda$ is an **Eigenvalue** and $v$ is an **Eigenvector**.
*   **Characteristic Polynomial**: $p(\lambda) = \det(A - \lambda I)$. Roots are eigenvalues.
*   **Diagonalization**: $A = PDP^{-1}$ if $A$ has $n$ linearly independent eigenvectors.
*   **Spectral Theorem**: Real symmetric matrices can be diagonalized by orthogonal matrices ($A = Q \Lambda Q^T$).

## 3. Norms and Inner Products

Measuring "length" and "angle".

### 3.1 Norms ($L_p$)
*   $L_1$ (Manhattan): $\sum |x_i|$.
*   $L_2$ (Euclidean): $\sqrt{\sum x_i^2}$.
*   $L_\infty$ (Max): $\max |x_i|$.

### 3.2 Inner Product
$\langle u, v \rangle = u^T v = \sum u_i v_i$.
*   **Orthogonality**: $\langle u, v \rangle = 0$.
*   **Cauchy-Schwarz Inequality**: $|\langle u, v \rangle| \le \|u\| \|v\|$.

## 4. Decompositions (The "Factorization" of LA)

Algorithms rely on decomposing difficult matrices into simpler ones.
1.  **LU Decomposition**: $A = LU$ (Lower $\times$ Upper). Used for solving linear systems.
2.  **QR Decomposition**: $A = QR$ (Orthogonal $\times$ Upper Triangular). Used for Least Squares.
3.  **Cholesky Decomposition**: $A = LL^T$ (for Symmetric Positive Definite).
4.  **SVD (Singular Value Decomposition)**: The "King" of decompositions. $A = U \Sigma V^T$.
    *   Exists for **any** matrix (even rectangular).
    *   Applications: Compression, PCA, Pseudo-inverse, Recommender Systems.
