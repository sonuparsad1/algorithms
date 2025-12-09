"""
Title: Stack (LIFO)
Topic: Data Structures

Theory:
    Last In, First Out (LIFO).
    Operations: push, pop, peek, is_empty.
    
    Implementations:
    1. Python List: Simplest (`append`, `pop`). Dynamic array.
    2. Arrays: Fixed size size logic (if simulation needed).
    
    Complexity:
    - Push/Pop: O(1) amortized.
"""

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def run_tests():
    s = Stack()
    s.push(10)
    s.push(20)
    
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()
    
    try:
        s.pop()
    except IndexError:
        print("Caught expected empty stack error")
    
    print("[PASS] Stack implementation")

if __name__ == "__main__":
    run_tests()
