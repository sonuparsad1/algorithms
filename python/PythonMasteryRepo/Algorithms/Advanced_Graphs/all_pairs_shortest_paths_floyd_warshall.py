"""
Title: Floyd-Warshall Algorithm
Topic: Advanced Graphs

Theory:
    All-Pairs Shortest Path.
    Dynamic Programming approach.
    Computes shortest path between every pair of vertices.
    
    Complexity: O(V^3).
"""

def floyd_warshall(graph_matrix):
    """
    Input: graph_matrix[i][j] = weight. infinity if no edge. 0 if i==j.
    Returns: dist matrix with shortest paths.
    """
    V = len(graph_matrix)
    # Deep copy
    dist = [row[:] for row in graph_matrix]
    
    for k in range(V): # Intermediate node
        for i in range(V): # Source
            for j in range(V): # Destination
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
    return dist

def run_tests():
    INF = float('inf')
    # Graph:
    # 0 -> 1 (5)
    # 0 -> 3 (10)
    # 1 -> 2 (3)
    # 2 -> 3 (1)
    
    matrix = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0]
    ]
    
    res = floyd_warshall(matrix)
    
    # Path 0 -> 3:
    # Direct: 10
    # Via 1,2: 0->1(5) -> 2(3) -> 3(1) = 9
    assert res[0][3] == 9
    
    print("[PASS] Floyd-Warshall")

if __name__ == "__main__":
    run_tests()
