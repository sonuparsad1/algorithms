"""
Title: Longest Palindromic Substring
Topic: String Algorithms

Theory:
    Find the longest substring which is a palindrome.
    Approaches:
    1. DP: O(N^2).
    2. Expand Around Center: O(N^2) but O(1) space.
    3. Manacher's Algorithm: O(N) (Too complex for basic study repo usually, implementing Expand Center).
"""

def longest_palindrome_expand(s):
    if not s: return ""
    start, end = 0, 0
    
    for i in range(len(s)):
        # Odd length
        len1 = expand_around_center(s, i, i)
        # Even length
        len2 = expand_around_center(s, i, i + 1)
        max_len = max(len1, len2)
        
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2
            
    return s[start:end+1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def run_tests():
    s = "babad"
    res = longest_palindrome_expand(s)
    # "bab" or "aba"
    assert res in ["bab", "aba"]
    
    print("[PASS] Longest Palindrome")

if __name__ == "__main__":
    run_tests()
