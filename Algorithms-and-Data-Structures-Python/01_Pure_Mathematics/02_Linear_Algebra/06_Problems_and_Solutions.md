# Linear Algebra: Problems and Solutions

## Problem 1: Number of Spanning Trees (Matrix Tree Theorem)

**Statement**: Given a connected graph $G$, calculate the number of distinct spanning trees.

**Theory (Kirchhoff's Theorem)**:
The number of spanning trees is equal to any cofactor of the **Laplacian Matrix** $L$.
$L = D - A$, where $D$ is Degree Matrix (diagonal), $A$ is Adjacency Matrix.

**Approach**:
1.  Construct $L$.
2.  Remove last row and last column to get $L'$.
3.  Compute $\det(L')$.

**Python Solution**:
```python
def count_spanning_trees(adj_matrix):
    n = len(adj_matrix)
    # 1. Build Laplacian
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        degree = sum(adj_matrix[i])
        for j in range(n):
            if i == j:
                L[i][j] = degree
            elif adj_matrix[i][j]:
                L[i][j] = -1
    
    # 2. Minor (Remove last row/col)
    minor = [row[:-1] for row in L[:-1]]
    
    # 3. Determinant (using our Matrix class logic)
    mat = Matrix(minor)
    return round(mat.determinant()) 
```

## Problem 2: Knight's Moves on Infinite Board

**Statement**: Can a Knight reach $(x, y)$ from $(0, 0)$? In exactly $K$ steps?
**Linear Algebra Approach**:
This is a path counting problem on a graph.
For small board: Adjacency Matrix power $A^K$.
For infinite board: Not strictly linear algebra matrices, but can be modeled as linear combination of move vectors.
$(x, y) = a(1, 2) + b(2, 1) + \dots$
More of a Diophantine / BFS problem, but $A^k$ applies for finite bounded boards (e.g., "Moves on Keypad").

## Problem 3: Recurrence with "Sum of Previous Terms"

**Statement**: $a_n = 2a_{n-1} + a_{n-2} + n^2$. Find $a_N \pmod M$.
**State Vector**: Need terms to generate next $n^2$ (which is $(n+1)^2 = n^2 + 2n + 1$).
$V_n = [a_n, a_{n-1}, n^2, n, 1]^T$.
**Transition**:
$a_{n+1} = 2a_n + a_{n-1} + (n+1)^2 = 2a_n + a_{n-1} + n^2 + 2n + 1$.
$(n+1)^2 = n^2 + 2n + 1$.
$(n+1) = n + 1$.
$1 = 1$.

Matrix M:
```
[2, 1, 1, 2, 1]
[1, 0, 0, 0, 0]
[0, 0, 1, 2, 1]
[0, 0, 0, 1, 1]
[0, 0, 0, 0, 1]
```
Compute $M^N \times V_0$.
