"""
Title: Sudoku Solver
Topic: Backtracking

Theory:
    Fill 9x9 grid so that each row, column, and 3x3 box contains digits 1-9.
    
    Complexity: Exponential.
"""

def solve_sudoku(board):
    """
    board: List[List[str]] ('.' for empty)
    Modifies board in-place. Returns True if solved.
    """
    for r in range(9):
        for c in range(9):
            if board[r][c] == '.':
                for char in "123456789":
                    if is_valid(board, r, c, char):
                        board[r][c] = char
                        if solve_sudoku(board):
                            return True
                        board[r][c] = '.' # Backtrack
                return False
    return True

def is_valid(board, r, c, char):
    for i in range(9):
        if board[r][i] == char: return False
        if board[i][c] == char: return False
        if board[3*(r//3) + i//3][3*(c//3) + i%3] == char: return False
    return True

def run_tests():
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    solve_sudoku(board)
    assert board[0][2] != "."
    print("[PASS] Sudoku Solver")

if __name__ == "__main__":
    run_tests()
