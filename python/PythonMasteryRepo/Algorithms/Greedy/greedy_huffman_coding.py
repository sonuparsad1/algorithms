"""
Title: Huffman Coding
Topic: Greedy Algorithms

Theory:
    Lossless data compression.
    Assigns variable-length codes to characters based on frequencies.
    More frequent chars -> Shorter codes.
    Uses Min-Heap to build Huffman Tree.
    
    Complexity: O(N log N).
"""

import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq = {}
    for char in text:
        freq[char] = freq.get(char, 0) + 1
        
    pq = [Node(char, f) for char, f in freq.items()]
    heapq.heapify(pq)
    
    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(pq, merged)
        
    return pq[0]

def generate_codes(root, current_code, codes):
    if root is None: return
    
    if root.char is not None:
        codes[root.char] = current_code
        return
    
    generate_codes(root.left, current_code + "0", codes)
    generate_codes(root.right, current_code + "1", codes)

def run_tests():
    text = "aaabbc"
    # a:3, b:2, c:1
    # Tree building...
    # c(1), b(2) -> merge(3). (c left 0, b right 1) ?? depends on heap stability
    # merge(3), a(3) -> root(6).
    
    root = build_huffman_tree(text)
    codes = {}
    generate_codes(root, "", codes)
    
    # 'a' (freq 3) should have short code (length 1 typically if others deeper)
    # 'c' and 'b' should be longer.
    assert len(codes['a']) < len(codes['c']) or len(codes['a']) == 1
    
    encoded = "".join(codes[char] for char in text)
    print(f"Codes: {codes}")
    print(f"Encoded 'aaabbc': {encoded}")
    
    print("[PASS] Huffman Coding")

if __name__ == "__main__":
    run_tests()
