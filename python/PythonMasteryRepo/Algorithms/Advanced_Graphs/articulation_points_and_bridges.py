"""
Title: Articulation Points and Bridges
Topic: Advanced Graphs

Theory:
    Articulation Point (Cut Vertex): Removing it increases connected components.
    Bridge (Cut Edge): Removing it increases CCs.
    
    Algorithm: DFS based (Tarjan's logic variant).
    - `disc`: discovery time.
    - `low`: lowest point reachable via back-edge.
    - Condition Bridge: `low[v] > disc[u]`
    - Condition AP: `low[v] >= disc[u]` (plus root check)
"""

class GraphBridges:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.time = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def find_bridges(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        parent = [-1] * self.V
        bridges = []
        
        def dfs(u):
            disc[u] = self.time
            low[u] = self.time
            self.time += 1
            
            for v in self.adj[u]:
                if v == parent[u]:
                    continue
                if disc[v] != -1:
                    low[u] = min(low[u], disc[v])
                else:
                    parent[v] = u
                    dfs(v)
                    low[u] = min(low[u], low[v])
                    if low[v] > disc[u]:
                        bridges.append((u, v))
        
        for i in range(self.V):
            if disc[i] == -1:
                dfs(i)
        return bridges

def run_tests():
    # 0--1--2
    # | /   |
    # 3     4
    #       |
    #       5
    g = GraphBridges(6)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 0) # 0-1-2 Triangle
    g.add_edge(0, 3) # 3 is leaf
    g.add_edge(2, 4) # Bridge to 4
    g.add_edge(4, 5) # Bridge to 5
    
    bridges = g.find_bridges()
    # Expect (0,3), (2,4), (4,5) (Order varies)
    
    # Normalize for check
    normalized = []
    for u, v in bridges:
        normalized.append(tuple(sorted((u, v))))
        
    assert (0, 3) in normalized
    assert (2, 4) in normalized
    assert (4, 5) in normalized
    assert (0, 1) not in normalized # Cycle edge
    
    print("[PASS] Bridges detection")

if __name__ == "__main__":
    run_tests()
