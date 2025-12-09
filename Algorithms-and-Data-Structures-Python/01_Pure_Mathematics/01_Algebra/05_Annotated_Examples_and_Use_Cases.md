# Algebra: Annotated Examples and Use Cases

## 1. Cryptography: Diffie-Hellman Key Exchange

**Theory**: Relies on the difficulty of the Discrete Logarithm Problem in a cyclic group.
**Scenario**: Alice and Bob want to share a secret key over an insecure channel.

**Step-by-Step**:
1.  **Public Parameters**: A large prime $p$ and a primitive root $g$ modulo $p$. (e.g., $p=23, g=5$).
2.  **Alice**: Chooses private secret $a = 6$.
    *   Computes public $A = g^a \pmod p = 5^6 \pmod{23} = 8$.
    *   Sends $A$ to Bob.
3.  **Bob**: Chooses private secret $b = 15$.
    *   Computes public $B = g^b \pmod p = 5^{15} \pmod{23} = 19$.
    *   Sends $B$ to Alice.
4.  **Shared Secret**:
    *   Alice computes $s = B^a \pmod p = 19^6 \pmod{23} = 2$.
    *   Bob computes $s = A^b \pmod p = 8^{15} \pmod{23} = 2$.

**Why it works**:
$(g^a)^b = g^{ab} = (g^b)^a \pmod p$.
An attacker sees $p, g, A, B$. To find $s$, they need $a$ or $b$, requiring discrete log solution.

## 2. RSA Encryption (Rivest-Shamir-Adleman)

**Theory**: Relies on the difficulty of factoring large numbers.
**Key Generation**:
1.  Choose primes $p, q$. Let $n = pq$.
2.  Compute $\phi(n) = (p-1)(q-1)$.
3.  Choose $e$ such that $\gcd(e, \phi(n)) = 1$.
4.  Compute $d$ such that $ed \equiv 1 \pmod{\phi(n)}$ using Extended Euclidean Algo.

**Use Case**:
*   Public Key: $(e, n)$.
*   Private Key: $d$.
*   Encrypt: $C = M^e \pmod n$.
*   Decrypt: $M = C^d \pmod n$.

**Visual Model**:
Think of encryption as putting a message in a box locked by a "multiplication" lock ($e$). The "division" key ($d$) unlocks it. But finding $d$ without $p, q$ is like trying to un-mix paint.

## 3. Error Detection: CRC (Cyclic Redundancy Check)

**Theory**: Polynomial division over $\mathbb{F}_2$.
**Process**:
1.  Message is treated as a polynomial $M(x)$.
2.  Generator polynomial $G(x)$ is fixed (standard specification).
3.  Multiply $M(x)$ by $x^k$ (shift) and calculate remainder $R(x) = M(x) \cdot x^k \pmod{G(x)}$.
4.  Send $M(x) \cdot x^k - R(x)$. This is divisible by $G(x)$.
5.  Receiver checks if received polynomial is divisible by $G(x)$.

## 4. Competitive Programming: N-th Fibonacci via Matrix Exponentiation

**Problem**: Find $F_{10^{18}} \pmod{10^9+7}$.
**Naive**: $O(N)$ iteration. TLE.
**Algebraic Approach**:
$$ \begin{pmatrix} F_{n+1} \\ F_n \end{pmatrix} = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix} \begin{pmatrix} F_n \\ F_{n-1} \end{pmatrix} $$
Let $M = \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}$. Then $\vec{v}_n = M^n \vec{v}_0$.
Use Binary Exponentiation for $M^n$. $O(\log n)$.
