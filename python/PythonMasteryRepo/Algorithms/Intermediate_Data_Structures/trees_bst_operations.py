"""
Title: Binary Search Tree (BST)
Topic: Data Structures

Theory:
    Properties:
    - Left subtree keys < Root key
    - Right subtree keys > Root key
    
    Complexity: O(h) where h is height.
    Worst case O(n) (Skewed tree).
"""

class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def run_tests():
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]
    for k in keys:
        root = insert(root, k)
        
    found = search(root, 60)
    assert found is not None
    assert found.val == 60
    
    not_found = search(root, 99)
    assert not_found is None
    
    print("[PASS] BST Operations")

if __name__ == "__main__":
    run_tests()
