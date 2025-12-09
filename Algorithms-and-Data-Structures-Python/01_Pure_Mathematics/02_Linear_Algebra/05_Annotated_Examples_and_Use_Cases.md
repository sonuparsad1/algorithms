# Linear Algebra: Annotated Examples and Use Cases

## 1. PageRank Algorithm (Google)

**Theory**: Finding the "importance" of nodes in a graph based on incoming links. Modeling the web as a Markov Chain.
**Linear Algebra Core**: Finding the **Principal Eigenvector** of the transition matrix.
$$ v_{t+1} = M v_t $$
where $M$ is the stochastic matrix (columns sum to 1).
**Stationary Distribution**: $v = Mv$. This means $v$ is an eigenvector with eigenvalue $\lambda = 1$.

**Process**:
1.  Construct adjacency matrix $A$.
2.  Normalize columns to get $M$.
3.  Add "damping factor" (teleportation) to ensure connectivity and existence of limit.
4.  Use **Power Iteration**: Repeatedly multiply $v$ by $M$ until convergence. The magnitude of components of $v$ represents Rank.

## 2. Dimensionality Reduction (PCA)

**Scenario**: You have a dataset with 100 features, but many are correlated. You want to visualize it in 2D.
**Technique**: Principal Component Analysis via **SVD**.
1.  Center data (subtract mean). Form matrix $X$ ($n \text{ samples} \times d \text{ features}$).
2.  Compute covariance matrix $C = \frac{1}{n} X^T X$.
3.  Compute Eigenvectors of $C$ (or SVD of $X$).
4.  The eigenvectors corresponding to largest eigenvalues are "Principal Components" (directions of max variance).
5.  Project $X$ onto these top 2 vectors.

## 3. Game Theory: Lights Out

**Problem**: A grid of lights. Pressing one toggles it and neighbors. Turn all off.
**Model**: System of linear equations over $\mathbb{F}_2$ (GF(2)).
$$ Ax = b $$
where $x$ is vector of button presses (1 or 0), $b$ is current state, $A$ describes effect of buttons.
**Solution**: Gaussian Elimination over GF(2).

## 4. Recommender Systems (Matrix Factorization)

**Scenario**: Users rating movies. Matrix $R$ (Users $\times$ Movies) is sparse.
**Goal**: Fill in blanks.
**Model**: Assume $R \approx U \times V^T$.
$U$: User preference vectors (latent factors).
$V$: Movie feature vectors.
**Solver**: Alternating Least Squares (ALS) or SVD-based approximation.
