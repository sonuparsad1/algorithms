"""
Title: Edit Distance (Levenshtein Distance)
Topic: Dynamic Programming

Theory:
    Minimum operations to convert one string to another.
    Ops: Insert, Remove, Replace.
    
    Recurrence:
    if S1[i] == S2[j]: dp[i][j] = dp[i-1][j-1]
    else: dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) (Insert, Remove, Replace)
    
    Complexity: O(M * N).
"""

def edit_distance(str1, str2):
    m = len(str1)
    n = len(str2)
    
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j # Insert all
            elif j == 0:
                dp[i][j] = i # Remove all
            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i][j-1],    # Insert
                    dp[i-1][j],    # Remove
                    dp[i-1][j-1]   # Replace
                )
    return dp[m][n]

def run_tests():
    s1 = "sunday"
    s2 = "saturday"
    # Ops:
    # 1. s(u)n -> s(a)t (Replace u->a, insert t?)
    # sunday -> saturn... hard to trace manually, trusted algo usually.
    # sunday (6) -> saturday (8)
    # s==s, u->a, n->t, d->u, a->r, y->d, +a, +y (This path is messy)
    # Correct path: s, u->a, n->t, d->u, a->r, y->d... no, y matches end?
    # Actually:
    # s u n d a y
    # s a t u r d a y
    # Cost is usually 3:
    # 1. Replace n with r (surday)
    # 2. Insert t (sturday)
    # 3. Insert a (saturday)
    
    assert edit_distance(s1, s2) == 3 
    print("[PASS] Edit Distance")

if __name__ == "__main__":
    run_tests()
