"""
Title: Dijkstra's Algorithm (Shortest Path)
Topic: Advanced Graphs

Theory:
    Finds shortest paths from source to all other vertices in a weighted graph with NON-NEGATIVE weights.
    Uses Priority Queue (Min-Heap).
    
    Complexity: O((V + E) log V) with Binary Heap.
"""

import heapq

def dijkstra(graph, start):
    # graph: dict {u: [(v, weight), ...]}
    
    # Priority Queue: stores (dist, u)
    pq = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    while pq:
        d, u = heapq.heappop(pq)
        
        # Optimization: Early exit if we found a shorter path to u already
        if d > distances[u]:
            continue
        
        for v, weight in graph[u]:
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                heapq.heappush(pq, (distances[v], v))
                
    return distances

def run_tests():
    # A --1-- B
    # |       |
    # 4       2
    # |       |
    # C --3-- D
    
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('D', 2)],
        'C': [('A', 4), ('D', 3)],
        'D': [('B', 2), ('C', 3)]
    }
    
    dists = dijkstra(graph, 'A')
    
    assert dists['A'] == 0
    assert dists['B'] == 1
    assert dists['C'] == 4 # Direct path A->C
    # Wait, A->B->D->C = 1 + 2 + 3 = 6. Direct is 4.
    
    assert dists['D'] == 3 # A->B->D = 1+2 = 3
    
    print("[PASS] Dijkstra Algorithm")

if __name__ == "__main__":
    run_tests()
