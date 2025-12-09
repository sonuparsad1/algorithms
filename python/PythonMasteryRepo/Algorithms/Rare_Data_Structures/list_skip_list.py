"""
Title: Skip List
Topic: Rare Data Structures

Theory:
    Probabilistic data structure. Alternative to balanced trees.
    Multiple layers of linked lists.
    Search/Insert/Delete: O(log n) average.
    Space: O(n).
"""

import random

class Node:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = Node(-1, max_level)
        self.level = 0
        
    def random_level(self):
        lvl = 0
        while random.random() < self.p and lvl < self.max_level:
            lvl += 1
        return lvl

    def insert(self, key):
        update = [None] * (self.max_level + 1)
        curr = self.header
        
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
            update[i] = curr
            
        curr = curr.forward[0]
        
        if curr is None or curr.key != key:
            rlevel = self.random_level()
            if rlevel > self.level:
                for i in range(self.level + 1, rlevel + 1):
                    update[i] = self.header
                self.level = rlevel
                
            new_node = Node(key, rlevel)
            for i in range(rlevel + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        curr = self.header
        for i in range(self.level, -1, -1):
            while curr.forward[i] and curr.forward[i].key < key:
                curr = curr.forward[i]
        curr = curr.forward[0]
        if curr and curr.key == key:
            return True
        return False

def run_tests():
    sl = SkipList(3, 0.5)
    sl.insert(3)
    sl.insert(6)
    sl.insert(7)
    sl.insert(9)
    # 3, 6, 7, 9
    
    assert sl.search(3)
    assert sl.search(6)
    assert not sl.search(10)
    
    print("[PASS] Skip List")

if __name__ == "__main__":
    run_tests()
