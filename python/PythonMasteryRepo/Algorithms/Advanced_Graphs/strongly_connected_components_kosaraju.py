"""
Title: Strongly Connected Components (Kosaraju's Algorithm)
Topic: Advanced Graphs

Theory:
    Finds SCCs in a directed graph.
    Logic:
    1. Perform DFS and store vertices in stack by finish time.
    2. Transpose the graph (reverse edges).
    3. Pop from stack and perform DFS on Transposed graph.
    
    Complexity: O(V + E).
"""

from collections import defaultdict

class KosarajuSCC:
    def __init__(self, V):
        self.V = V
        self.adj = defaultdict(list)

    def add_edge(self, u, v):
        self.adj[u].append(v)
    
    def _fill_order(self, v, visited, stack):
        visited.add(v)
        for i in self.adj[v]:
            if i not in visited:
                self._fill_order(i, visited, stack)
        stack.append(v)
    
    def _get_transpose(self):
        g = KosarajuSCC(self.V)
        for i in self.adj:
            for j in self.adj[i]:
                g.add_edge(j, i)
        return g
    
    def _dfs_util(self, v, visited, component):
        visited.add(v)
        component.append(v)
        for i in self.adj[v]:
            if i not in visited:
                self._dfs_util(i, visited, component)
                
    def get_sccs(self):
        stack = []
        visited = set()
        
        # 1. Fill Stack
        for i in range(self.V):
            if i not in visited:
                self._fill_order(i, visited, stack)
                
        # 2. Transpose
        gr = self._get_transpose()
        
        # 3. Process Stack
        visited = set()
        sccs = []
        
        while stack:
            i = stack.pop()
            if i not in visited:
                component = []
                gr._dfs_util(i, visited, component)
                sccs.append(component)
        return sccs

def run_tests():
    # 0->2, 2->1, 1->0 (SCC 0,1,2)
    # 0->3, 3->4 (SCC 3, 4 separate)
    g = KosarajuSCC(5)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(1, 0)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    sccs = g.get_sccs()
    
    # Sort for checking
    sccs = [sorted(c) for c in sccs]
    # We expect [[0,1,2], [3], [4]] or similar order
    assert [0, 1, 2] in sccs
    assert [3] in sccs
    assert [4] in sccs
    
    print("[PASS] Kosaraju SCC")

if __name__ == "__main__":
    run_tests()
