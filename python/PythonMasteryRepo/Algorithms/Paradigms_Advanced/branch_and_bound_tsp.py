"""
Title: Branch and Bound (TSP)
Topic: Paradigms

Theory:
    Optimization problems.
    Explore branches of state space tree.
    Compute lower/upper bound. Prune if bound is worse than current best solution.
    
    Demo: TSP simplified logic explanation (Full TSP B&B is huge).
"""

# Very simplified B&B demonstration for Assignment Problem or similar
# Implementing a small exhaustive search with pruning logic for TSP
# 4 cities. 

def tsp_bnb(graph):
    n = len(graph)
    visited = [False] * n
    visited[0] = True
    min_cost = [float('inf')]
    
    def backtrack(curr, count, cost):
        if count == n and graph[curr][0] > 0:
            min_cost[0] = min(min_cost[0], cost + graph[curr][0])
            return

        # Pruning
        if cost >= min_cost[0]:
            return

        for i in range(n):
            if not visited[i] and graph[curr][i] > 0:
                visited[i] = True
                backtrack(i, count + 1, cost + graph[curr][i])
                visited[i] = False

    backtrack(0, 1, 0)
    return min_cost[0]

def run_tests():
    # 0 --10-- 1
    # |      / |
    # 20   35  25
    # |  /     |
    # 3 --30-- 2
    # Matrix:
    #   0   1   2   3
    # 0 0   10  15  20
    # 1 10  0   35  25
    # 2 15  35  0   30
    # 3 20  25  30  0
    
    graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]
    # Path: 0->1->3->2->0 = 10+25+30+15 = 80
    # Path: 0->2->3->1->0 = 15+30+25+10 = 80
    # Path: 0->1->2->3->0 = 10+35+30+20 = 95
    
    res = tsp_bnb(graph)
    assert res == 80
    print("[PASS] Branch and Bound TSP")

if __name__ == "__main__":
    run_tests()
