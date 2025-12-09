"""
Title: Subset Sum Problem
Topic: Dynamic Programming

Theory:
    Determine if there is a subset of the given set with sum equal to given sum.
    
    Recurrence:
    dp[i][j] = dp[i-1][j] (Excluding item) OR dp[i-1][j-item] (Including item)
    
    Complexity: O(N * Sum).
"""

def is_subset_sum(arr, n, sum_val):
    dp = [[False for _ in range(sum_val + 1)] for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][0] = True # Sum 0 is always possible (empty set)
        
    for i in range(1, n + 1):
        for j in range(1, sum_val + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j - arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
                
    return dp[n][sum_val]

def run_tests():
    set_vals = [3, 34, 4, 12, 5, 2]
    sum_val = 9
    assert is_subset_sum(set_vals, len(set_vals), sum_val) is True
    assert is_subset_sum(set_vals, len(set_vals), 30) is False # Maybe true?
    # 34 too big. 3+4+12+5+2 = 26. So 30 impossible.
    
    print("[PASS] Subset Sum")

if __name__ == "__main__":
    run_tests()
