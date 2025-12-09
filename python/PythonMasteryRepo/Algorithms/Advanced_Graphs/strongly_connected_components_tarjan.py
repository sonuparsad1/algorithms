"""
Title: Strongly Connected Components (Tarjan's Algorithm)
Topic: Advanced Graphs

Theory:
    Finds SCCs in one DFS pass.
    Maintains `discovery_time` and `low_link` value for each node.
    
    low_link[u] = lowest discovery time reachable from u (including back-edges in stack).
    If low_link[u] == disc[u], u is root of an SCC.
    
    Complexity: O(V + E).
"""

class TarjanSCC:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for _ in range(V)]
        self.time = 0

    def add_edge(self, u, v):
        self.adj[u].append(v)
        
    def _scc_util(self, u, low, disc, stack_member, stack, start_node=None): 
        # Note: start_node not really needed inside, just standard logic
        disc[u] = self.time
        low[u] = self.time
        self.time += 1
        stack_member[u] = True
        stack.append(u)
        
        for v in self.adj[u]:
            if disc[v] == -1: # Not visited
                self._scc_util(v, low, disc, stack_member, stack)
                low[u] = min(low[u], low[v])
            elif stack_member[v]: # Back-edge
                low[u] = min(low[u], disc[v])
                
        # Head of SCC
        if low[u] == disc[u]:
            w = -1
            component = []
            while w != u:
                w = stack.pop()
                component.append(w)
                stack_member[w] = False
            self.sccs.append(component)

    def find_sccs(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        self.sccs = []
        
        for i in range(self.V):
            if disc[i] == -1:
                self._scc_util(i, low, disc, stack_member, stack)
        return self.sccs

def run_tests():
    g = TarjanSCC(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    sccs = g.find_sccs()
    sccs = [sorted(c) for c in sccs]
    
    assert [0, 1, 2] in sccs
    assert [3] in sccs
    assert [4] in sccs
    
    print("[PASS] Tarjan SCC")

if __name__ == "__main__":
    run_tests()
