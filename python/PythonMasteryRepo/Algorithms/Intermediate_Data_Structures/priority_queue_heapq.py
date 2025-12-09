"""
Title: Priority Queue (Heapq)
Topic: Data Structures

Theory:
    Elements are popped based on priority (min or max).
    Python `heapq` module implements a Min-Heap on top of a list.
    
    Complexity:
    - Push: O(log n)
    - Pop: O(log n)
    - Peek: O(1)
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.count = 0 
        
    def push(self, item, priority):
        # heapq is min-heap.
        # Store as tuple (priority, count, item) to handle comparison safely.
        # 'count' breaks ties without comparing 'item' which might not be comparable.
        heapq.heappush(self.heap, (priority, self.count, item))
        self.count += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty PQ")
        return heapq.heappop(self.heap)[2] # Return item

    def is_empty(self):
        return len(self.heap) == 0

def run_tests():
    pq = PriorityQueue()
    pq.push("Task Low", 10)
    pq.push("Task High", 1)
    pq.push("Task Med", 5)
    
    # Expect 1, 5, 10
    assert pq.pop() == "Task High"
    assert pq.pop() == "Task Med"
    assert pq.pop() == "Task Low"
    
    print("[PASS] Priority Queue (Min Heap)")

if __name__ == "__main__":
    run_tests()
