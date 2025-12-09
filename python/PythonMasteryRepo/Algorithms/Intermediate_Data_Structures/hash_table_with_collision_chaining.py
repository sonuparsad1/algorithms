"""
Title: Hash Table (Collision Handling: Chaining)
Topic: Data Structures

Theory:
    Map Keys to Values using a hash function.
    Collision: When two keys map to same index.
    Chaining: Use a linked list at each index (bucket) to store multiple items.
    
    Complexity:
    - Average key access: O(1 + load_factor).
    - Worst case: O(n) (if all keys hash to same bucket).
"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTableChaining:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        head = self.buckets[idx]
        
        # Check update
        curr = head
        while curr:
            if curr.key == key:
                curr.value = value
                return
            curr = curr.next
            
        # Insert at front
        new_node = Node(key, value)
        new_node.next = head
        self.buckets[idx] = new_node

    def get(self, key):
        idx = self._hash(key)
        curr = self.buckets[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

def run_tests():
    ht = HashTableChaining()
    ht.put("Alice", 100)
    ht.put("Bob", 90)
    ht.put("Alice", 101) # Update
    
    assert ht.get("Alice") == 101
    assert ht.get("Bob") == 90
    assert ht.get("Charlie") is None
    
    print("[PASS] Hash Table (Chaining)")

if __name__ == "__main__":
    run_tests()
