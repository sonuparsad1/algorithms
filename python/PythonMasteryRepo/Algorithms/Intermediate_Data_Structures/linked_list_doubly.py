"""
Title: Doubly Linked List
Topic: Data Structures

Theory:
    Nodes have `prev` and `next` pointers.
    Allows traversal in both directions.
    
    Complexity:
    - Delete given node: O(1) (if reference known)
    - Extra space for `prev` pointer.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
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
        new_node.prev = last

    def delete_node(self, node):
        """Assumes node belongs to this list."""
        if not node:
            return

        if node == self.head:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        
        if node.prev:
            node.prev.next = node.next

    def to_list_forward(self):
        out = []
        curr = self.head
        while curr:
            out.append(curr.data)
            curr = curr.next
        return out

def run_tests():
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    
    assert dll.to_list_forward() == [10, 20, 30]
    
    # Delete middle node (20)
    # Finding node manually for test
    node_20 = dll.head.next 
    dll.delete_node(node_20)
    
    assert dll.to_list_forward() == [10, 30]
    
    # Check links
    assert dll.head.next.data == 30
    assert dll.head.next.prev.data == 10
    
    print("[PASS] Doubly Linked List")

if __name__ == "__main__":
    run_tests()
