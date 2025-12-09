"""
Title: Bellman-Ford Algorithm
Topic: Advanced Graphs

Theory:
    Finds shortest paths from source to all vertices.
    Can handle NEGATIVE weights.
    Detects Negative Cycles.
    
    Algorithm: Relax all E edges, V-1 times.
    
    Complexity: O(V * E).
"""

def bellman_ford(vertices, edges, start):
    # edges: list of (u, v, weight)
    distances = {v: float('inf') for v in vertices}
    distances[start] = 0
    
    # Relax V-1 times
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if distances[u] != float('inf') and distances[u] + w < distances[v]:
                distances[v] = distances[u] + w
                
    # Detect negative cycle
    for u, v, w in edges:
        if distances[u] != float('inf') and distances[u] + w < distances[v]:
            raise ValueError("Negative Cycle Detected")
            
    return distances

def run_tests():
    vertices = ['A', 'B', 'C']
    edges = [
        ('A', 'B', -1),
        ('B', 'C', 2),
        ('C', 'A', 4) # Cycle A->B->C->A cost: -1+2+4 = 5 (Positive cycle OK)
    ]
    
    dists = bellman_ford(vertices, edges, 'A')
    assert dists['B'] == -1
    assert dists['C'] == 1
    
    # Negative Cycle Case
    bad_edges = [
        ('A', 'B', 1),
        ('B', 'C', -5),
        ('C', 'A', 2) # 1 - 5 + 2 = -2 (Negative Cycle)
    ]
    try:
        bellman_ford(vertices, bad_edges, 'A')
    except ValueError as e:
        print(f"Caught expected error: {e}")

    print("[PASS] Bellman-Ford")

if __name__ == "__main__":
    run_tests()
