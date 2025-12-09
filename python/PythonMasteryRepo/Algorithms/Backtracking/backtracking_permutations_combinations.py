"""
Title: Permutations and Combinations (Backtracking)
Topic: Backtracking

Theory:
    Permutations: Order matters. (n!)
    Combinations: Order does not matter. nCk.
"""

def generate_permutations(nums):
    res = []
    
    def backtrack(start):
        if start == len(nums):
            res.append(nums[:])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            backtrack(start + 1)
            nums[start], nums[i] = nums[i], nums[start] # Backtrack
            
    backtrack(0)
    return res

def generate_combinations(n, k):
    res = []
    
    def backtrack(start, current):
        if len(current) == k:
            res.append(current[:])
            return
            
        for i in range(start, n + 1):
            current.append(i)
            backtrack(i + 1, current)
            current.pop()
            
    backtrack(1, [])
    return res

def run_tests():
    # Permutations of [1,2] -> [1,2], [2,1]
    perms = generate_permutations([1, 2])
    assert len(perms) == 2
    
    # Combinations of 4 choose 2 -> 6
    # (1,2), (1,3), (1,4), (2,3), (2,4), (3,4)
    combs = generate_combinations(4, 2)
    assert len(combs) == 6
    
    print("[PASS] Permutations and Combinations")

if __name__ == "__main__":
    run_tests()
