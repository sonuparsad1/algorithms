"""
Title: 0/1 Knapsack Problem
Topic: Dynamic Programming

Theory:
    Given weights and values of n items, put these items in a knapsack of capacity W 
    to get the maximum total value.
    Item can either be taken (1) or left (0).
    
    Recurrence:
    K(n, W) = max(
        val[n-1] + K(n-1, W-wt[n-1]),  // Include item
        K(n-1, W)                      // Exclude item
    )
    
    Complexity: O(N * W).
"""

def knapsack_01(W, wt, val, n):
    # dp[i][w] stores max value with i items and capacity w
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i-1] <= w:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]
                
    return dp[n][W]

def run_tests():
    val = [60, 100, 120]
    wt = [10, 20, 30]
    W = 50
    n = len(val)
    # Expected: 20+30 weights (100+120=220)
    assert knapsack_01(W, wt, val, n) == 220
    print("[PASS] 0/1 Knapsack")

if __name__ == "__main__":
    run_tests()
