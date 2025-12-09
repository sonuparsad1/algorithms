"""
Title: Graph Traversals (BFS & DFS)
Topic: Advanced Graphs

Theory:
    BFS (Breadth First Search):
    - Uses Queue.
    - Exploration level by level.
    - Application: Shortest Path in unweighted graph.
    - Complexity: O(V + E).

    DFS (Depth First Search):
    - Uses Stack (Recursion).
    - Exploration deep into branches.
    - Application: Cycle detection, Path finding, Topological Sort logic.
    - Complexity: O(V + E).
"""

from collections import deque

class Graph:
    def __init__(self, edges, bidirectional=True):
        self.adj = {}
        for u, v in edges:
            self.add_edge(u, v, bidirectional)

    def add_edge(self, u, v, bidirectional):
        if u not in self.adj: self.adj[u] = []
        if v not in self.adj: self.adj[v] = []
        
        self.adj[u].append(v)
        if bidirectional:
            self.adj[v].append(u)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        traversal = []
        
        while queue:
            node = queue.popleft()
            traversal.append(node)
            
            # Neighbors
            for neighbor in self.adj.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return traversal

    def dfs(self, start):
        visited = set()
        traversal = []
        self._dfs_recursive(start, visited, traversal)
        return traversal

    def _dfs_recursive(self, node, visited, traversal):
        visited.add(node)
        traversal.append(node)
        
        for neighbor in self.adj.get(node, []):
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited, traversal)

def run_tests():
    # 0 -- 1
    # |    |
    # 2 -- 3 -- 4
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    g = Graph(edges)
    
    bfs_res = g.bfs(0)
    # BFS from 0: 0, then 1,2, then 3, then 4
    # Note: Neighbor order depends on list, assume sorted insertion or specific order in test:
    # Neighbors of 0: 1, 2
    # Neighbors of 1: 0, 3
    # Neighbors of 2: 0, 3
    # Neighbors of 3: 1, 2, 4
    assert bfs_res[0] == 0
    assert 1 in bfs_res[1:3] and 2 in bfs_res[1:3]
    assert 4 == bfs_res[-1]
    
    dfs_res = g.dfs(0)
    assert dfs_res[0] == 0
    assert len(dfs_res) == 5
    
    print("[PASS] BFS and DFS")

if __name__ == "__main__":
    run_tests()
