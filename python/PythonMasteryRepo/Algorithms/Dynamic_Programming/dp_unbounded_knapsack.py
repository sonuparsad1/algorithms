"""
Title: Unbounded Knapsack
Topic: Dynamic Programming

Theory:
    Similar to 0/1 Knapsack, but we can pick an item MULTIPLE times.
    
    Recurrence:
    dp[w] = max(dp[w], dp[w-wt[i]] + val[i]) for all items.
    
    Complexity: O(N * W).
"""

def unbounded_knapsack(W, n, val, wt):
    dp = [0] * (W + 1)
    
    for w in range(W + 1):
        for i in range(n):
            if wt[i] <= w:
                dp[w] = max(dp[w], dp[w - wt[i]] + val[i])
                
    return dp[W]

def run_tests():
    W = 100
    val = [10, 30, 20]
    wt = [5, 10, 15]
    n = len(val)
    
    # We can take item 1 (wt 10, val 30) 10 times -> val 300.
    # Or item 0 (wt 5, val 10) 20 times -> val 200.
    # Unbounded, so max is 300.
    assert unbounded_knapsack(W, n, val, wt) == 300
    print("[PASS] Unbounded Knapsack")

if __name__ == "__main__":
    run_tests()
