"""
Title: Segment Tree
Topic: Rare Data Structures

Theory:
    Range Queries (Min, Max, Sum) with Updates.
    Tree structure where leaves are array elements.
    O(log n) per op.
"""

class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (4 * self.n)
        self._build(data, 0, 0, self.n - 1)

    def _build(self, data, node, start, end):
        if start == end:
            self.tree[node] = data[start]
        else:
            mid = (start + end) // 2
            self._build(data, 2 * node + 1, start, mid)
            self._build(data, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2] # Sum Query Example

    def update(self, idx, val):
        self._update(0, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if start <= idx <= mid:
                self._update(2 * node + 1, start, mid, idx, val)
            else:
                self._update(2 * node + 2, mid + 1, end, idx, val)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, l, r):
        return self._query(0, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if l <= start and end <= r:
            return self.tree[node]
        mid = (start + end) // 2
        p1 = self._query(2 * node + 1, start, mid, l, r)
        p2 = self._query(2 * node + 2, mid + 1, end, l, r)
        return p1 + p2

def run_tests():
    data = [1, 3, 5, 7, 9, 11]
    st = SegmentTree(data)
    
    # Sum(1..3) = 3+5+7 = 15
    assert st.query(1, 3) == 15
    
    st.update(1, 10)
    # Sum(1..3) = 10+5+7 = 22
    assert st.query(1, 3) == 22
    
    print("[PASS] Segment Tree")

if __name__ == "__main__":
    run_tests()
