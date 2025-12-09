"""
Abstract Algebra Algorithms Implementation.

Includes:
1. Permutation Class (Composition, Power, Cycles).
2. Burnside's Lemma Solver (for Rotational/Dihedral symmetries).
3. Landau's Function (Max Order of Permutation).
"""

from typing import List, Tuple
from math import gcd

# ==============================================================================
# 1. Permutation Operations
# ==============================================================================

class Permutation:
    def __init__(self, mapping: List[int]):
        # mapping[i] is the image of i. Assumes 0-indexed elements 0..N-1
        self.mapping = mapping
        self.n = len(mapping)
        
    def __repr__(self):
        return f"Perm({self.mapping})"

    def __mul__(self, other: 'Permutation') -> 'Permutation':
        # Composition: (f * g)(x) = f(g(x))
        if self.n != other.n:
            raise ValueError("Size mismatch")
        new_map = [self.mapping[other.mapping[i]] for i in range(self.n)]
        return Permutation(new_map)

    def get_cycles(self) -> List[List[int]]:
        visited = [False] * self.n
        cycles = []
        for i in range(self.n):
            if not visited[i]:
                cycle = []
                curr = i
                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = self.mapping[curr]
                cycles.append(cycle)
        return cycles

    def power(self, k: int) -> 'Permutation':
        # Apply permutation k times using cycle decomposition
        # O(N) instead of O(N log K) composition
        new_map = [0] * self.n
        cycles = self.get_cycles()
        
        for cycle in cycles:
            l = len(cycle)
            shift = k % l
            for idx, val in enumerate(cycle):
                # The element at 'val' moves to cycle[(idx + shift) % l]
                # Wait: mapping[i] is where i goes.
                # If i is cycle[idx], it goes to cycle[idx+1].
                # After k steps, it lands at cycle[(idx + k) % l].
                target = cycle[(idx + shift) % l]
                new_map[val] = target # val goes to target
                
        return Permutation(new_map)

# ==============================================================================
# 2. Burnside's Lemma / Polya Helpers
# ==============================================================================

def count_necklace_embeddings(n: int, k: int) -> int:
    """
    Count distinct necklaces with n beads and k colors under Rotation.
    Formula: (1/n) * sum(k^gcd(i, n) for i in 1..n)
    """
    total = 0
    for i in range(1, n + 1):
        cycles = gcd(i, n)
        total += k ** cycles
    return total // n

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def landau_function_dp(n: int) -> int:
    """
    Computes g(n): Maximum order of an element of S_n.
    Equivalent to Max LCM of partitions of n.
    DP State: dp[i] = sets of possible LCMs summing to i? Too big.
    Optimization: The partition consists of prime powers.
    dp[j] = max LCM using sum j.
    """
    # Primes up to n
    primes = []
    is_prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
            for i in range(p*p, n+1, p): is_prime[i] = False
            
    # dp[w] = max_lcm with weight w
    dp = [1.0] * (n + 1) # Use float to avoid huge int overhead during intermediate steps? No, Python ints are fine.
    dp_int = [1] * (n + 1)
    
    # Knapsack-like approach
    for p in primes:
        for w in range(n, -1, -1):
            pp = p
            while pp <= w:
                dp_int[w] = max(dp_int[w], dp_int[w - pp] * pp)
                pp *= p
                
    return max(dp_int)

if __name__ == "__main__":
    # Test Permutation
    p = Permutation([1, 2, 0, 4, 3]) 
    # Cycles: (0 1 2), (3 4)
    # Order: LCM(3, 2) = 6. P^6 should be identity.
    p6 = p.power(6)
    assert p6.mapping == [0, 1, 2, 3, 4]
    
    # Test Necklace
    # 3 beads, 2 colors (Red, Blue)
    # Patterns: RRR, BBB, RRB(x3->1), BBR(x3->1). Total 4.
    # Formula: 1/3 * (2^gcd(1,3) + 2^gcd(2,3) + 2^gcd(3,3)) = 1/3 * (2^1 + 2^1 + 2^3) = 1/3 * (2+2+8) = 12/3 = 4.
    assert count_necklace_embeddings(3, 2) == 4
    
    # Test Landau
    # g(4) -> partition 4 into max lcm. 4->4, 3+1->3, 2+2->2, 2+1+1->2. Max is 4.
    # g(5) -> 2,3 -> lcm 6.
    assert landau_function_dp(5) == 6
    
    print("Abstract Algebra Implementations Verified.")
