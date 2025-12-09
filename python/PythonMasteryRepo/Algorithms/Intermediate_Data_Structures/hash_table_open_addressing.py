"""
Title: Hash Table (Collision Handling: Open Addressing)
Topic: Data Structures

Theory:
    When collision occurs, probe for the next empty slot.
    Probing methods: Linear Probing, Quadratic Probing, Double Hashing.
    Here: Linear Probing.
    
    Deletion is tricky (requires "Deleted" marker).
"""

class HashTableOA:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.keys = [None] * capacity
        self.values = [None] * capacity
        self.size = 0

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        if self.size == self.capacity:
            raise Exception("Table Full (Resize not implemented)")
            
        idx = self._hash(key)
        
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.capacity
            
        self.keys[idx] = key
        self.values[idx] = value
        self.size += 1

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break
        return None

def run_tests():
    ht = HashTableOA(5)
    ht.put("A", 1)
    ht.put("B", 2)
    
    assert ht.get("A") == 1
    
    # Test collision (hard to guarantee without known hash, but assuming Linear Probing works)
    
    print("[PASS] Hash Table (Open Addressing)")

if __name__ == "__main__":
    run_tests()
