"""
Title: KMP Algorithm (Knuth-Morris-Pratt)
Topic: String Algorithms

Theory:
    Pattern searching that avoids unnecessary comparisons using LPS array (Longest Prefix Suffix).
    LPS[i] = length of the longest proper prefix of pat[0..i] that is also a suffix of pat[0..i].
    
    Complexity: O(N) time, O(M) space.
"""

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0 # Length of previous longest prefix suffix
    i = 1
    
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    matches = []
    
    i = 0 # text index
    j = 0 # pattern index
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            matches.append(i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return matches

def run_tests():
    txt = "ABABDABACDABABCABAB"
    pat = "ABABCABAB"
    matches = kmp_search(txt, pat)
    assert matches == [10]
    print("[PASS] KMP Search")

if __name__ == "__main__":
    run_tests()
