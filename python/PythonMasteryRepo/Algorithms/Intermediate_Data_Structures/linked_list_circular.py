"""
Title: Circular Linked List
Topic: Data Structures

Theory:
    The last node points back to the head (or another node) instead of None.
    
    Use case:
    - Round Robin scheduling.
    - Implementation of queues.
    
    Pitfall: Infinite loops during traversal if break condition not set correctly.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            curr = self.head
            while curr.next != self.head:
                curr = curr.next
            curr.next = new_node
            new_node.next = self.head

    def to_list(self):
        if not self.head:
            return []
        out = []
        curr = self.head
        while True:
            out.append(curr.data)
            curr = curr.next
            if curr == self.head:
                break
        return out

def run_tests():
    cll = CircularLinkedList()
    cll.append("A")
    cll.append("B")
    cll.append("C")
    
    assert cll.to_list() == ["A", "B", "C"]
    
    # Check cycle
    head = cll.head
    assert head.next.next.next == head
    
    print("[PASS] Circular Linked List")

if __name__ == "__main__":
    run_tests()
