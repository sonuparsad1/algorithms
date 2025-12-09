"""
Title: Eulerian and Hamiltonian Paths
Topic: Advanced Graphs

Theory:
    Eulerian Path: Visits every EDGE exactly once.
    - Cond: 0 or 2 vertices have odd degree. All non-zero degree vertices connected.
    
    Eulerian Circuit: Starts and ends same vertex.
    - Cond: All vertices have even degree.
    
    Hamiltonian Path: Visits every VERTEX exactly once.
    - NP-Complete problem generally. Backtracking is best approach.
"""

def is_eulerian_path_possible(n, edges):
    degree = [0] * n
    for u, v in edges:
        degree[u] += 1
        degree[v] += 1 # Undirected
        
    odd_count = 0
    for d in degree:
        if d % 2 != 0:
            odd_count += 1
            
    if odd_count == 0:
        return "Circuit"
    elif odd_count == 2:
        return "Path"
    else:
        return "None"

def run_tests():
    # Square: 0-1, 1-2, 2-3, 3-0. All degree 2. Circuit.
    edges_sq = [(0,1), (1,2), (2,3), (3,0)]
    assert is_eulerian_path_possible(4, edges_sq) == "Circuit"
    
    # Line: 0-1-2. 0(1), 1(2), 2(1). Odd=2. Path.
    edges_line = [(0,1), (1,2)]
    assert is_eulerian_path_possible(3, edges_line) == "Path"

    # Star: Center 0 con to 1,2,3. 0(3), others(1). Odd=4. None.
    edges_star = [(0,1), (0,2), (0,3)]
    assert is_eulerian_path_possible(4, edges_star) == "None"
    
    print("[PASS] Eulerian Logic")

if __name__ == "__main__":
    run_tests()
