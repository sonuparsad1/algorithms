"""
Title: Matrix Chain Multiplication
Topic: Dynamic Programming

Theory:
    Given sequence of matrices, find most efficient way to multiply (parenthesize) them.
    Cost is number of scalar multiplications.
    
    Recurrence:
    m[i,j] = min(m[i,k] + m[k+1,j] + p[i-1]*p[k]*p[j]) for k in i to j-1.
    
    Complexity: O(N^3).
"""

def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for L in range(2, n + 1): # L is chain length
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = float('inf')
            
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if q < m[i][j]:
                    m[i][j] = q
                    
    return m[1][n]

def run_tests():
    # Matrices dimensions: 1x2, 2x3, 3x4
    # p = [1, 2, 3, 4]
    # (A*B)*C or A*(B*C)
    # (1x2 * 2x3) -> 1x3, cost 1*2*3 = 6. Then (1x3 * 3x4) -> 1x4, cost 1*3*4=12. Total 18.
    # A*(2x3 * 3x4) -> 2x4, cost 2*3*4 = 24. Then (1x2 * 2x4) -> 1x4, cost 1*2*4=8. Total 32.
    # Min is 18.
    
    arr = [1, 2, 3, 4]
    assert matrix_chain_order(arr) == 18
    print("[PASS] Matrix Chain Multiplication")

if __name__ == "__main__":
    run_tests()
