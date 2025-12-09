"""
Title: LRU Cache Implementation
Topic: Rare Data Structures

Theory:
    Least Recently Used cache eviction policy.
    Uses Hash Map + Doubly Linked List.
    Get/Put: O(1).
    Python's `OrderedDict` makes this trivial, but we implement manually or wrap it.
"""

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) # Mark as recently used
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False) # Remove first (least recent)

def run_tests():
    lru = LRUCache(2)
    lru.put(1, 1)
    lru.put(2, 2)
    assert lru.get(1) == 1 # 1 moved to end. Order: 2, 1
    
    lru.put(3, 3) # Evicts 2 (Least recent)
    assert lru.get(2) == -1
    
    lru.put(4, 4) # Evicts 1 (Least recent, since 3 was put)
    # Order was 1, 3. Now 3, 4.
    assert lru.get(1) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    
    print("[PASS] LRU Cache")

if __name__ == "__main__":
    run_tests()
