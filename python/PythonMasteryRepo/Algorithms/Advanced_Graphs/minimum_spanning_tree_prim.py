"""
Title: Minimum Spanning Tree (Prim's Algorithm)
Topic: Advanced Graphs

Theory:
    Greedy approach.
    Start from a vertex, grow the tree by adding nearest vertex not yet in tree.
    Uses Priority Queue.
    
    Complexity: O(E log V) with Binary Heap.
"""

import heapq

def prim(n, graph):
    # graph: {u: [(v, weight), ...]}
    # n: number of vertices, assumed 0 to n-1
    
    start_node = 0
    pq = [(0, start_node, -1)] # (weight, node, parent)
    visited = [False] * n
    mst_weight = 0
    mst_edges = []
    
    while pq:
        w, u, parent = heapq.heappop(pq)
        
        if visited[u]:
            continue
            
        visited[u] = True
        mst_weight += w
        if parent != -1:
            mst_edges.append((parent, u, w))
            
        for v, weight in graph.get(u, []):
            if not visited[v]:
                heapq.heappush(pq, (weight, v, u))
                
    return mst_edges, mst_weight

def run_tests():
    # Same graph
    # 0: (1,1), (2,3)
    # 1: (0,1), (3,1)
    # 2: (0,3), (3,1)
    # 3: (1,1), (2,1)
    
    graph = {
        0: [(1, 1), (2, 3)],
        1: [(0, 1), (3, 1)],
        2: [(0, 3), (3, 1)],
        3: [(1, 1), (2, 1)]
    }
    
    edges, weight = prim(4, graph)
    
    assert weight == 3
    # Check edges exist
    # 0-1 (1), 1-3 (1), 3-2 (1) is a valid path picking order
    # Edges: (0,1,1), (1,3,1), (3,2,1)
    
    print("[PASS] Prim MST")

if __name__ == "__main__":
    run_tests()
