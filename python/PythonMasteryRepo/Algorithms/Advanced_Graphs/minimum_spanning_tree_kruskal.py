"""
Title: Minimum Spanning Tree (Kruskal's Algorithm)
Topic: Advanced Graphs

Theory:
    Finds MST of a connected, undirected, weighted graph.
    Greedy approach:
    1. Sort all edges by weight.
    2. Add edge if it doesn't form a cycle (Use DSU).
    
    Complexity: O(E log E) or O(E log V).
"""

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            if self.rank[root_i] < self.rank[root_j]:
                self.parent[root_i] = root_j
            elif self.rank[root_i] > self.rank[root_j]:
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] = root_i
                self.rank[root_i] += 1
            return True
        return False

def kruskal(n, edges):
    # edges: list of (u, v, weight)
    # Sort by weight
    edges.sort(key=lambda x: x[2])
    
    dsu = DSU(n)
    mst = []
    mst_weight = 0
    
    for u, v, w in edges:
        if dsu.union(u, v):
            mst.append((u, v, w))
            mst_weight += w
            
    return mst, mst_weight

def run_tests():
    # 0 --1-- 1
    # |       |
    # 3       1
    # |       |
    # 2 --1-- 3
    
    # Cycle 0-1-3-2-0.
    edges = [
        (0, 1, 1),
        (1, 3, 1),
        (2, 3, 1),
        (0, 2, 3) # Expensive edge
    ]
    # Vertices: 0, 1, 2, 3 (n=4)
    # MST should pick the three 1-weight edges. Total 3.
    
    mst, weight = kruskal(4, edges)
    
    assert weight == 3
    assert len(mst) == 3
    # Ensure expensive edge not in MST
    assert (0, 2, 3) not in mst
    
    print("[PASS] Kruskal MST")

if __name__ == "__main__":
    run_tests()
