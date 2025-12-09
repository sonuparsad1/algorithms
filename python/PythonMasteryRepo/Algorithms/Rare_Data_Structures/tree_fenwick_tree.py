"""
Title: Fenwick Tree (Binary Indexed Tree)
Topic: Rare Data Structures

Theory:
    Prefix sums and updates in O(log n).
    `update(i, delta)`: Adds delta to element at i.
    `query(i)`: Returns sum from 0 to i.
"""

class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        # 1-based indexing used internally often
        i += 1 
        while i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)

    def query(self, i):
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

def run_tests():
    # [1, 2, 3, 4]
    ft = FenwickTree(4)
    data = [1, 2, 3, 4]
    for i, x in enumerate(data):
        ft.update(i, x)
        
    # Sum(0..2) = 1+2+3 = 6
    assert ft.query(2) == 6
    # Sum(0..3) = 10
    assert ft.query(3) == 10
    
    # Update index 1 by +2 (becomes 4) -> [1, 4, 3, 4]
    ft.update(1, 2)
    # Sum(0..2) = 1+4+3 = 8
    assert ft.query(2) == 8
    
    print("[PASS] Fenwick Tree")

if __name__ == "__main__":
    run_tests()
