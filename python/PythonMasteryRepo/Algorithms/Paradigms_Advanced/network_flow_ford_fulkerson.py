"""
Title: Ford-Fulkerson Algorithm (Max Flow)
Topic: Paradigms

Theory:
    Computes Max Flow in valid flow network.
    Iteratively find augmenting paths in Residual Graph and add flow.
    Uses DFS (which can be slow, O(E*f*), hence Edmonds-Karp is preferred).
"""

class GraphFF:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        
    def dfs(self, u, t, visited, parent):
        visited[u] = True
        if u == t: return True
        
        for v, capacity in enumerate(self.graph[u]):
            if not visited[v] and capacity > 0:
                parent[v] = u
                if self.dfs(v, t, visited, parent):
                    return True
        return False
        
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        
        # While there is a path from s to t
        while True:
            visited = [False] * self.ROW
            if not self.dfs(source, sink, visited, parent):
                break
                
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            
            # Update residual graph
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
                
        return max_flow

def run_tests():
    # 0 -> 1 (16), 0 -> 2 (13)
    # 1 -> 2 (10), 1 -> 3 (12)
    # 2 -> 1 (4), 2 -> 4 (14)
    # 3 -> 2 (9), 3 -> 5 (20)
    # 4 -> 3 (7), 4 -> 5 (4)
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    g = GraphFF(graph)
    assert g.ford_fulkerson(0, 5) == 23
    print("[PASS] Ford Fulkerson")

if __name__ == "__main__":
    run_tests()
