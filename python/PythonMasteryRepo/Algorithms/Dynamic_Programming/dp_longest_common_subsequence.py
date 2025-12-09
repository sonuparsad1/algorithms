"""
Title: Longest Common Subsequence (LCS)
Topic: Dynamic Programming

Theory:
    Find the length of the longest subsequence present in both strings.
    Subsequence: Order matters, continuity does not.
    
    Recurrence:
    if S1[i] == S2[j]: 1 + LCS(i-1, j-1)
    else: max(LCS(i-1, j), LCS(i, j-1))
    
    Complexity: O(M * N).
"""

def lcs(X, Y):
    m = len(X)
    n = len(Y)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
    return dp[m][n]

def run_tests():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    # LCS is "GTAB", length 4
    assert lcs(s1, s2) == 4
    print("[PASS] LCS")

if __name__ == "__main__":
    run_tests()
