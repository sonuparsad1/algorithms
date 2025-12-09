"""
Title: Suffix Tree (Intro)
Topic: String Algorithms

Theory:
    Compressed Trie of all suffixes of the given text.
    Extremely powerful (Pattern matching O(M), Longest Repeating Substr, etc).
    
    Implementation note: Full O(N) Ukkonen's algo is very complex.
    Here we implement a Naive Suffix Tree (O(N^2)) for educational purpose.
"""

class SuffixTrieNode:
    def __init__(self):
        self.children = {}
        self.indexes = [] # Store starting indexes of suffixes passing through

    def insert(self, suffix, idx):
        self.indexes.append(idx)
        if not suffix:
            return
        first = suffix[0]
        if first not in self.children:
            self.children[first] = SuffixTrieNode()
        self.children[first].insert(suffix[1:], idx)

    def search(self, pattern):
        if not pattern:
            return self.indexes
        first = pattern[0]
        if first in self.children:
            return self.children[first].search(pattern[1:])
        return []

class NaiveSuffixTree:
    def __init__(self, text):
        self.root = SuffixTrieNode()
        for i in range(len(text)):
            self.root.insert(text[i:], i)

def run_tests():
    txt = "banana"
    # Suffixes: banana, anana, nana, ana, na, a
    st = NaiveSuffixTree(txt)
    
    # Search "ana"
    idxs = st.root.search("ana")
    idxs.sort()
    # "ana" starts at 1 (anana), 3 (ana)
    assert idxs == [1, 3]
    
    print("[PASS] Suffix Tree Naive")

if __name__ == "__main__":
    run_tests()
