"""
Title: Queue (FIFO)
Topic: Data Structures

Theory:
    First In, First Out (FIFO).
    Operations: enqueue, dequeue.
    
    Implementations:
    1. `collections.deque`: Doubly Linked List based. O(1) ends.
    2. `list`: Bad for queues! `pop(0)` is O(n).
"""

from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft() # O(1)

    def is_empty(self):
        return len(self.items) == 0

def run_tests():
    q = Queue()
    q.enqueue("First")
    q.enqueue("Second")
    
    assert q.dequeue() == "First"
    assert q.dequeue() == "Second"
    
    print("[PASS] Queue implementation")

if __name__ == "__main__":
    run_tests()
