"""
Title: Trie (Prefix Tree)
Topic: String Algorithms

Theory:
    Tree data structure used for storing strings efficiently.
    Each node represents a character.
    Useful for: Autocomplete, Spell Checker.
    
    Complexity: Insert/Search O(K) where K is key length.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def run_tests():
    t = Trie()
    t.insert("apple")
    assert t.search("apple") is True
    assert t.search("app") is False
    assert t.starts_with("app") is True
    
    t.insert("app")
    assert t.search("app") is True
    
    print("[PASS] Trie Basics")

if __name__ == "__main__":
    run_tests()
