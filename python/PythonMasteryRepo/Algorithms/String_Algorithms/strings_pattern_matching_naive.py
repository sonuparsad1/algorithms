"""
Title: Naive Pattern Searching
Topic: String Algorithms

Theory:
    Slide the pattern over text one by one and check for a match.
    
    Complexity: O(M * (N - M + 1)) -> O(N*M) worst case.
    Best case (no match): O(N).
"""

def naive_search(text, pattern):
    n = len(text)
    m = len(pattern)
    matches = []
    
    for i in range(n - m + 1):
        if text[i : i + m] == pattern:
            matches.append(i)
    return matches

def run_tests():
    txt = "AABAACAADAABAABA"
    pat = "AABA"
    # Matches at 0, 9, 12
    res = naive_search(txt, pat)
    assert res == [0, 9, 12]
    print("[PASS] Naive Pattern Search")

if __name__ == "__main__":
    run_tests()
