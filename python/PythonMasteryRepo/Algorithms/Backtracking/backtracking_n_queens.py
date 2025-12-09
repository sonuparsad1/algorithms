"""
Title: N-Queens Problem
Topic: Backtracking

Theory:
    Place N queens on NxN board such that no two queens attack each other.
    Constraint: No row, column, or diagonal sharing.
    
    Complexity: O(N!).
"""

def solve_n_queens(n):
    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    
    # Tracking sets for efficiency
    cols = set()
    diag1 = set() # (r - c)
    diag2 = set() # (r + c)
    
    def backtrack(r):
        if r == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue
                
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            board[r][c] = 'Q'
            
            backtrack(r + 1)
            
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
            board[r][c] = '.'
            
    backtrack(0)
    return solutions

def run_tests():
    # 4-Queens has 2 distinct solutions
    sols = solve_n_queens(4)
    assert len(sols) == 2
    
    print("[PASS] N-Queens")

if __name__ == "__main__":
    run_tests()
