"""
Title: Activity Selection Problem
Topic: Greedy Algorithms

Theory:
    Select max number of activities that can be performed by a single person.
    Assumption: Activities sorted by FINISH time.
    If not sorted, sort them first.
    
    Greedy Choice: Always pick next activity that finishes earliest and is compatible.
    Complexity: O(N log N) (due to sorting).
"""

def max_activities(activities):
    # format: (start, finish)
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish = activities[0][1]
    
    for i in range(1, len(activities)):
        start, finish = activities[i]
        if start >= last_finish:
            selected.append(activities[i])
            last_finish = finish
            
    return selected

def run_tests():
    # (start, finish)
    acts = [(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
    # Sorted by finish:
    # (1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9) (Finish: 2, 4, 6, 7, 9, 9)
    # 1. Pick (1,2). Finish 2.
    # 2. Pick (3,4). Start 3 >= 2. Ok. Finish 4.
    # 3. (0,6) Start 0 < 4. No.
    # 4. (5,7) Start 5 >= 4. Ok. Finish 7.
    # 5. (8,9) Start 8 >= 7. Ok. Finish 9.
    # Total 4.
    
    res = max_activities(acts)
    assert len(res) == 4
    print("[PASS] Activity Selection")

if __name__ == "__main__":
    run_tests()
