# Abstract Algebra: Group Actions and Combinatorics

## 1. Group Actions

While basic algebra checks satisfying properties (Is this a Group?), **Group Actions** study how groups **act** on sets. This is the bridge to Combinatorics and Geometry.

### 1.1 Definition
Left action of group $G$ on set $X$ is a function $G \times X \to X$, denoted $g \cdot x$, satisfying:
1.  **Identity**: $e \cdot x = x$.
2.  **Compatibility**: $(gh) \cdot x = g \cdot (h \cdot x)$.

### 1.2 Orbits and Stabilizers
*   **Orbit** of $x$: $Orb(x) = \{g \cdot x \mid g \in G\}$. The set of points $x$ can reach.
*   **Stabilizer** of $x$: $Stab(x) = \{g \in G \mid g \cdot x = x\}$. The set of group elements that fix $x$.
*   **Orbit-Stabilizer Theorem**: $|G| = |Orb(x)| \cdot |Stab(x)|$.

## 2. Burnside's Lemma (The "Counting Lemma")

Used to count distinct objects under symmetry (e.g., how many distinct necklaces with 3 beads exist?).
The number of distinct orbits $|X/G|$ is the average number of elements fixed by each $g \in G$.

$$ |X/G| = \frac{1}{|G|} \sum_{g \in G} |fix(g)| $$
where $fix(g) = \{x \in X \mid g \cdot x = x\}$.

## 3. Pólya Enumeration Theorem (PET)

A generalization of Burnside's Lemma that counts distinct colorings by "weight" (e.g., 2 Red, 1 Blue).
*   **Cycle Index Polynomial** $Z(G)$: A polynomial representing the cycle structure of $G$'s permutations.
    $$ Z(G) = \frac{1}{|G|} \sum_{g \in G} t_1^{j_1(g)} t_2^{j_2(g)} \dots $$
    where $j_k(g)$ is the number of cycles of length $k$ in permutation $g$.
*   **Theorem**: Determine the number of patterns by substituting color weights into $Z(G)$.

## 4. Permutation Groups

*   **Symmetric Group $S_n$**: All $n!$ permutations of $n$ elements.
*   **Alternating Group $A_n$**: Only even permutations.
*   **Cayley's Theorem**: Every group is isomorphic to a subgroup of a symmetric group. 

## 5. Sylow Theorems (Structure of Finite Groups)

If $|G| = p^k m$ ($p$ prime not dividing $m$), then:
1.  **Existence**: $G$ has a subgroup of size $p^k$ (Sylow $p$-subgroup).
2.  **Conjugacy**: All Sylow $p$-subgroups are conjugate.
3.  **Counting**: Number of Sylow $p$-subgroups $n_p$ satisfies $n_p \equiv 1 \pmod p$ and $n_p \mid m$.

**Application**: Used to prove a group is not simple (normal subgroups exist).
