"""
Title: Job Sequencing Problem
Topic: Greedy Algorithms

Theory:
    Given jobs with (deadline, profit). Each job takes 1 unit of time.
    Maximize total profit such that all selected jobs finish before deadlines.
    
    Algorithm:
    1. Sort by Profit (Desc).
    2. Assign to latest possible time slot available before deadline.
"""

def job_sequencing(jobs, max_deadline):
    # jobs: list of (id, deadline, profit)
    jobs.sort(key=lambda x: x[2], reverse=True)
    
    slots = [-1] * (max_deadline + 1)
    total_profit = 0
    job_order = []
    
    for job in jobs:
        jid, deadline, profit = job
        # Find free slot from deadline down to 1
        for j in range(min(max_deadline, deadline), 0, -1):
            if slots[j] == -1:
                slots[j] = jid
                total_profit += profit
                break
                
    job_order = [x for x in slots if x != -1]
    return job_order, total_profit

def run_tests():
    # (id, deadline, profit)
    jobs = [('a', 2, 100), ('b', 1, 19), ('c', 2, 27), ('d', 1, 25), ('e', 3, 15)]
    # Sort: a(100), c(27), d(25), b(19), e(15)
    
    # 1. a(100) d=2. Slot 2 free? Yes. slots[2]=a.
    # 2. c(27) d=2. Slot 2 taken. Slot 1 free? Yes. slots[1]=c.
    # 3. d(25) d=1. Slot 1 taken. 
    # 4. b(19) d=1. Slot 1 taken.
    # 5. e(15) d=3. Slot 3 free? Yes. slots[3]=e.
    
    # Order: c, a, e. Profit 27+100+15 = 142.
    
    order, profit = job_sequencing(jobs, 3)
    assert profit == 142
    assert set(order) == {'a', 'c', 'e'}
    
    print("[PASS] Job Sequencing")

if __name__ == "__main__":
    run_tests()
