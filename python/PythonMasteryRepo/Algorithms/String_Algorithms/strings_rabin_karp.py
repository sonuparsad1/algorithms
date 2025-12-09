"""
Title: Rabin-Karp Algorithm
Topic: String Algorithms

Theory:
    Uses Rolling Hash to find exact matches.
    Calculate hash of pattern and first window of text.
    Slide window, update hash in O(1).
    
    Complexity: O(N + M) average. O(NM) worst case (Hash collisions).
"""

def rabin_karp(text, pattern):
    d = 256 # Alphabets
    q = 101 # Prime number
    n = len(text)
    m = len(pattern)
    p = 0 # hash for pattern
    t = 0 # hash for text
    h = 1
    matches = []
    
    # h = pow(d, m-1) % q
    for i in range(m - 1):
        h = (h * d) % q
        
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        
    for i in range(n - m + 1):
        if p == t:
            if text[i:i+m] == pattern:
                matches.append(i)
        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return matches

def run_tests():
    txt = "GEEKS FOR GEEKS"
    pat = "GEEK"
    matches = rabin_karp(txt, pat)
    assert matches == [0, 10]
    print("[PASS] Rabin-Karp")

if __name__ == "__main__":
    run_tests()
