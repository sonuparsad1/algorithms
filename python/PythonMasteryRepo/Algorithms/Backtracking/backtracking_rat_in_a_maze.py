"""
Title: Rat in a Maze
Topic: Backtracking

Theory:
    Find a path from source (0,0) to destination (N-1, N-1).
    Movement allowed: Down, Right (or more).
    Blockages: 0 (or specific value).
    
    Complexity: O(2^(N^2)).
"""

def rat_in_maze(maze):
    n = len(maze)
    sol = [[0 for _ in range(n)] for _ in range(n)]
    
    if solve_maze_util(maze, 0, 0, sol, n) == False:
        return []
    return sol

def is_safe(maze, x, y, n):
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 1

def solve_maze_util(maze, x, y, sol, n):
    if x == n - 1 and y == n - 1 and maze[x][y] == 1:
        sol[x][y] = 1
        return True
        
    if is_safe(maze, x, y, n):
        if sol[x][y] == 1: return False # Already visited
        
        sol[x][y] = 1 # Mark
        
        # Move Forward (Down)
        if solve_maze_util(maze, x + 1, y, sol, n): return True
        # Move Forward (Right)
        if solve_maze_util(maze, x, y + 1, sol, n): return True
        
        sol[x][y] = 0 # Backtrack
        return False
        
    return False

def run_tests():
    maze = [
        [1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]
    ]
    path = rat_in_maze(maze)
    # Expected path (1s): (0,0)->(1,0)->(1,1)->(2,1)->(3,1)->(3,2)->(3,3)
    assert path[0][0] == 1
    assert path[3][3] == 1
    assert path[0][1] == 0
    print("[PASS] Rat in Maze")

if __name__ == "__main__":
    run_tests()
