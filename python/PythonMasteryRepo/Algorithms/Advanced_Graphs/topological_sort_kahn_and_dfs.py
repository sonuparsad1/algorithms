"""
Title: Topological Sort (Kahn's and DFS)
Topic: Advanced Graphs

Theory:
    Linear ordering of vertices in a DAG (Directed Acyclic Graph).
    For every edge u -> v, u comes before v.
    
    Algorithms:
    1. Kahn's (BFS): Uses in-degrees. Can detect cycles.
    2. DFS: Use stack (finish time).
    
    Complexity: O(V + E).
"""

from collections import deque

def kahn_topological_sort(n, adj):
    in_degree = [0] * n
    for u in adj:
        for v in adj[u]:
            in_degree[v] += 1
            
    queue = deque([i for i in range(n) if in_degree[i] == 0])
    topo_order = []
    
    while queue:
        u = queue.popleft()
        topo_order.append(u)
        
        for v in adj.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)
                
    if len(topo_order) != n:
        raise ValueError("Graph has a cycle!")
        
    return topo_order

def run_tests():
    # 5 -> 2, 5 -> 0
    # 4 -> 0, 4 -> 1
    # 2 -> 3
    # 3 -> 1
    
    adj = {
        5: [2, 0],
        4: [0, 1],
        2: [3],
        3: [1],
        0: [],
        1: []
    }
    # n=6 (include 0,1,2,3,4,5)
    
    order = kahn_topological_sort(6, adj)
    
    # Valid order: 5 comes before 2 and 0. 4 comes before 0 and 1. 
    # One valid: 4, 5, 2, 3, 1, 0
    # Or: 5, 4, 2, 3, 1, 0
    
    print(f"Topo Order: {order}")
    
    # Check dependencies
    pos = {node: i for i, node in enumerate(order)}
    assert pos[5] < pos[2]
    assert pos[2] < pos[3]
    assert pos[3] < pos[1]
    
    print("[PASS] Topological Sort")

if __name__ == "__main__":
    run_tests()
