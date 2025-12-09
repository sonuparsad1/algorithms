"""
Title: Bloom Filter
Topic: Rare Data Structures

Theory:
    Probabilistic data structure for set membership.
    False Positives possible. False Negatives IMPOSSIBLE.
    Uses multiple hash functions and a bit array.
"""

import hashlib

class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _get_hashes(self, item):
        hashes = []
        digest = hashlib.md5(str(item).encode('utf-8')).hexdigest()
        # Create multiple fake independent hashes from one MD5
        # (Simplified approach)
        base = int(digest, 16)
        for i in range(self.hash_count):
            hashes.append((base + i * 1337) % self.size)
        return hashes

    def add(self, item):
        for h in self._get_hashes(item):
            self.bit_array[h] = 1

    def contains(self, item):
        for h in self._get_hashes(item):
            if self.bit_array[h] == 0:
                return False
        return True # Possibly True

def run_tests():
    bf = BloomFilter(100, 3)
    bf.add("apple")
    bf.add("banana")
    
    assert bf.contains("apple")
    assert bf.contains("banana")
    assert not bf.contains("cherry") # Small chance of False Positive, but with 100 bits vs 2 items, practically 0
    print("[PASS] Bloom Filter")

if __name__ == "__main__":
    run_tests()
