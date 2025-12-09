"""
Title: Disjoint Set Union (DSU)
Topic: Data Structures

Theory:
    Efficiently manage disjoint sets and determine connectivity.
    Operations:
    - `find(x)`: Find representative of set containing x.
    - `union(x, y)`: Merge sets containing x and y.
    
    Optimizations:
    - Path Compression (Flatten tree during find).
    - Union by Rank/Size (Attach smaller tree to larger).
    
    Complexity: O(alpha(n)) - Nearly constant time.
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            # Path Compression
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            # Union by Rank
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True # Merged
        return False # Already same set

def run_tests():
    dsu = DSU(5)
    # 0, 1, 2, 3, 4
    
    dsu.union(0, 1)
    dsu.union(2, 3)
    
    assert dsu.find(0) == dsu.find(1)
    assert dsu.find(2) == dsu.find(3)
    assert dsu.find(0) != dsu.find(2)
    
    dsu.union(1, 2)
    # Now all 0, 1, 2, 3 should be connected
    assert dsu.find(0) == dsu.find(3)
    
    print("[PASS] DSU (Union Find)")

if __name__ == "__main__":
    run_tests()
