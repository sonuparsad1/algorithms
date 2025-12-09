"""
Title: Treap (Tree + Heap)
Topic: Rare Data Structures

Theory:
    Randomized Binary Search Tree.
    Each node has a Key (BST property) and Priority (Heap property).
    Priorities are random -> High probability of O(log n) height.
    operations: Split and Merge.
"""

import random

class TreapNode:
    def __init__(self, key):
        self.key = key
        self.priority = random.random()
        self.left = None
        self.right = None

def split(root, key):
    """
    Splits treap into two:
    - Left: Keys <= key
    - Right: Keys > key
    """
    if root is None:
        return None, None
    
    if root.key <= key:
        right_split, remaining = split(root.right, key)
        root.right = right_split
        return root, remaining
    else:
        left_split, remaining = split(root.left, key)
        root.left = remaining
        return left_split, root

def merge(left, right):
    """
    Merges two treaps (all keys in left < all keys in right).
    """
    if left is None: return right
    if right is None: return left
    
    if left.priority > right.priority: # Max Heap
        left.right = merge(left.right, right)
        return left
    else:
        right.left = merge(left, right.left)
        return right

def insert(root, key):
    if root is None:
        return TreapNode(key)
    
    # Split by key
    left, right = split(root, key)
    # Insert new node in middle
    new_node = TreapNode(key)
    return merge(merge(left, new_node), right)

def traverse(root, res):
    if root:
        traverse(root.left, res)
        res.append(root.key)
        traverse(root.right, res)

def run_tests():
    root = None
    keys = [10, 20, 5, 80, 40]
    for k in keys:
        root = insert(root, k)
        
    res = []
    traverse(root, res)
    assert res == sorted(keys)
    print("[PASS] Treap Insertion and Traversal")

if __name__ == "__main__":
    run_tests()
