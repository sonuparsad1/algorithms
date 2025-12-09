"""
Title: Iterator and Generator Patterns
Topic: Design Patterns

Theory:
    Iterator Pattern: Provide a way to access elements of an aggregate object uniformly without exposing underlying representation.
    
    Python's Protocol: `__iter__` and `__next__`.
    Generator: A simpler way to create iterators using `yield`.
"""

# ==========================================
# 1. Classic Iterator (Class-based)
# ==========================================

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        val = self.current
        self.current -= 1
        return val

# ==========================================
# 2. Generator (Function-based)
# ==========================================

def count_up(limit):
    """Yields numbers from 1 to limit."""
    n = 1
    while n <= limit:
        yield n
        n += 1

def run_tests():
    # Iterator
    c = CountDown(3)
    assert list(c) == [3, 2, 1]
    
    # Generator
    g = count_up(3)
    assert list(g) == [1, 2, 3]
    
    print("[PASS] Iterator and Generator")

if __name__ == "__main__":
    run_tests()
