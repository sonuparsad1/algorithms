"""
Title: Longest Increasing Subsequence (LIS)
Topic: Dynamic Programming

Theory:
    Find length of the longest subsequence that is strictly increasing.
    
    Approaches:
    1. DP O(N^2): dp[i] = 1 + max(dp[j]) for j < i if arr[j] < arr[i].
    2. Binary Search O(N log N): Patience sorting optimization (tail array).
"""

import bisect

# 1. DP Approach O(N^2)
def lis_dp(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    return max(dp) if arr else 0

# 2. Binary Search Approach O(N log N)
def lis_binary_search(arr):
    if not arr: return 0
    tails = []
    
    for x in arr:
        idx = bisect.bisect_left(tails, x)
        if idx < len(tails):
            tails[idx] = x
        else:
            tails.append(x)
    return len(tails)

def run_tests():
    arr = [10, 22, 9, 33, 21, 50, 41, 60]
    # LIS: 10, 22, 33, 50, 60 or ...
    # Length 5
    
    assert lis_dp(arr) == 5
    assert lis_binary_search(arr) == 5
    print("[PASS] LIS")

if __name__ == "__main__":
    run_tests()
