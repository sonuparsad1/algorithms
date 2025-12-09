"""
Title: Min/Max Heap Operations (Manual Implementation)
Topic: Data Structures

Theory:
    Binary Heap using Array.
    Parent(i) = (i-1)//2
    Left(i) = 2*i + 1
    Right(i) = 2*i + 2
    
    Max Heap: Parent >= Children
"""

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        root = self.heap[0]
        self.heap[0] = self.heap.pop() # Move last to root
        self._sift_down(0)
        return root

    def _sift_up(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def _sift_down(self, idx):
        n = len(self.heap)
        smallest = idx
        l = 2 * idx + 1
        r = 2 * idx + 2
        
        if l < n and self.heap[l] < self.heap[smallest]:
            smallest = l
        if r < n and self.heap[r] < self.heap[smallest]:
            smallest = r
            
        if smallest != idx:
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx]
            self._sift_down(smallest)

def run_tests():
    h = MinHeap()
    h.push(10)
    h.push(5)
    h.push(30)
    h.push(2)
    
    # Heap: [2, 5, 30, 10] (One possible structure)
    assert h.pop() == 2
    assert h.pop() == 5
    assert h.pop() == 10
    assert h.pop() == 30
    
    print("[PASS] Min Heap manual implementation")

if __name__ == "__main__":
    run_tests()
