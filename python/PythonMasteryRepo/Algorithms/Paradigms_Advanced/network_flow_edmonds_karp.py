"""
Title: Edmonds-Karp Algorithm (Max Flow)
Topic: Paradigms

Theory:
    Implementation of Ford-Fulkerson using BFS.
    Guarantees shortest augmenting path (in terms of edges).
    Complexity: O(V * E^2).
"""

from collections import deque

class GraphEK:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)
        
    def bfs(self, s, t, parent):
        visited = [False] * self.ROW
        queue = deque([s])
        visited[s] = True
        parent[s] = -1
        
        while queue:
            u = queue.popleft()
            for v, cap in enumerate(self.graph[u]):
                if not visited[v] and cap > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t: return True
        return False
        
    def edmonds_karp(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float('inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow

def run_tests():
    # Same graph
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    g = GraphEK(graph)
    assert g.edmonds_karp(0, 5) == 23
    print("[PASS] Edmonds Karp")

if __name__ == "__main__":
    run_tests()
