"""
Title: Singly Linked List
Topic: Data Structures

Theory:
    Linear collection of nodes. Each node points to the next.
    
    Complexity:
    - Access: O(n)
    - Insert/Delete at beginning: O(1)
    - Insert/Delete at end: O(n) (or O(1) if tail pointer maintained)
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, key):
        curr = self.head
        
        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        
        if curr is None:
            return # key not found

        prev.next = curr.next
        curr = None

    def to_list(self):
        out = []
        curr = self.head
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out

def run_tests():
    ll = SinglyLinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(0) # 0, 1, 2
    
    assert ll.to_list() == [0, 1, 2]
    
    ll.delete_value(1) # 0, 2
    assert ll.to_list() == [0, 2]
    
    ll.delete_value(0) # 2
    assert ll.to_list() == [2]
    
    print("[PASS] Singly Linked List")

if __name__ == "__main__":
    run_tests()
