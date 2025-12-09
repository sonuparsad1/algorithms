"""
Title: Subset Generation (Backtracking)
Topic: Backtracking

Theory:
    Generate all subsets (Power Set) of a given set.
    
    Complexity: O(2^N).
"""

def generate_subsets(nums):
    res = []
    
    def backtrack(start, current_subset):
        res.append(current_subset[:])
        
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()
            
    backtrack(0, [])
    return res

def run_tests():
    nums = [1, 2, 3]
    subs = generate_subsets(nums)
    # Expected length 2^3 = 8
    # [], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
    assert len(subs) == 8
    assert [] in subs
    assert [1, 2, 3] in subs
    
    print("[PASS] Subset Generation")

if __name__ == "__main__":
    run_tests()
