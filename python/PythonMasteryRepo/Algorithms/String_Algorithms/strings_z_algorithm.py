"""
Title: Z Algorithm
Topic: String Algorithms

Theory:
    Linear time pattern matching.
    Z-array: Z[i] is the length of the longest substring starting from S[i] which is also a prefix of S.
    Concat P + "$" + T. If Z[i] == len(P), occurrence found.
    
    Complexity: O(M + N).
"""

def get_z_array(string):
    n = len(string)
    z = [0] * n
    l, r = 0, 0
    
    for i in range(1, n):
        if i > r:
            l, r = i, i
            while r < n and string[r] == string[r - l]:
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if z[k] < r - i + 1:
                z[i] = z[k]
            else:
                l = i
                while r < n and string[r] == string[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1
    return z

def z_search(text, pattern):
    concat = pattern + "$" + text
    l = len(concat)
    z = get_z_array(concat)
    matches = []
    
    for i in range(l):
        if z[i] == len(pattern):
            matches.append(i - len(pattern) - 1)
    return matches

def run_tests():
    txt = "BAABAXAABA"
    pat = "AABA"
    matches = z_search(txt, pat)
    assert matches == [1, 7]
    print("[PASS] Z Algorithm")

if __name__ == "__main__":
    run_tests()
