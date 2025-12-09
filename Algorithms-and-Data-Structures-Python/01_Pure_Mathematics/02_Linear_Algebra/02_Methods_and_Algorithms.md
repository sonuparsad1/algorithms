# Linear Algebra: Methods and Algorithms

## 1. Gaussian Elimination

**Purpose**: Solve $Ax = b$, find $\det(A)$, find $A^{-1}$, find Rank.
**Method**: Transform augmented matrix $[A|b]$ to Row Echelon Form (REF) and then Reduced REF (RREF).
**Operations**:
1.  Swap rows.
2.  Multiply row by non-zero scalar.
3.  Add multiple of one row to another.
**Complexity**: $O(N^3)$.

## 2. Matrix Multiplication Optimization

Naive is $O(N^3)$.
*   **Strassen's Algorithm**: $O(N^{\log_2 7}) \approx O(N^{2.81})$. Uses recursive block multiplication tricks.
*   **Coppersmith-Winograd**: $O(N^{2.376})$ (Theoretical, huge constant).

## 3. Computing Matrix Powers $A^k$

**Method**: Binary Exponentiation (Square and Multiply).
**Complexity**: $O(N^3 \log k)$.
**Application**: Counting paths of length $k$ in a graph, Linear Recurrences.

## 4. Singular Value Decomposition (SVD) Algorithm

**Goal**: Find $U, \Sigma, V^T$ such that $A = U \Sigma V^T$.
**Iterative Methods**:
*   **Golub-Kahan-Reinsch**: Reduces $A$ to bidiagonal form, then uses QR-like iterations.
*   **Power Iteration**: Finds dominant eigenvalue/vector. Can be adapted for SVD.

## 5. Solving Linear Recurrences (The General Method)

Given $f_n = c_1 f_{n-1} + \dots + c_k f_{n-k}$.
1.  Construct Transformation Matrix $T$ size $k \times k$.
$$
T = \begin{bmatrix}
c_1 & c_2 & \dots & c_{k-1} & c_k \\
1 & 0 & \dots & 0 & 0 \\
0 & 1 & \dots & 0 & 0 \\
\vdots & & \ddots & & \vdots \\
0 & 0 & \dots & 1 & 0
\end{bmatrix}
$$
2.  State vector $V_{n-1} = [f_{n-1}, \dots, f_{n-k}]^T$.
3.  $V_{n+m} = T^{m+1} V_{n-1}$.

## 6. Least Squares Regression

Given overdetermined system $Ax = b$ (more equations than unknowns).
Minimize $\|Ax - b\|^2$.
**Analytical Solution**: Normal Equation $A^T A x = A^T b$.
**computional Note**: Solving via Normal Equation is unstable if condition number is high. QR decomposition or SVD is preferred ($x = A^+ b$).

## 7. Linear Basis (Competitive Programming)

**Problem**: Given a set of integers, find max XOR subset, check if $X$ can be formed by XORing subset.
**Algorithm**: Gaussian Elimination on bits ($GF(2)$).
Maintain a basis set $\{b_1, \dots, b_d\}$ where each basis vector improves the "highest bit".
**Complexity**: $O(N \log (\max val))$.
