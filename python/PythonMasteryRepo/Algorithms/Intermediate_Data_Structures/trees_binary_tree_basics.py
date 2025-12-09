"""
Title: Binary Tree Basics
Topic: Data Structures

Theory:
    Hierarchical structure.
    Traversals:
    - Preorder (Root, Left, Right)
    - Inorder (Left, Root, Right)
    - Postorder (Left, Right, Root)
    - Level Order (BFS)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    if root:
        res = inorder_traversal(root.left)
        res.append(root.val)
        res = res + inorder_traversal(root.right)
    return res

def preorder_traversal(root):
    res = []
    if root:
        res.append(root.val)
        res = res + preorder_traversal(root.left)
        res = res + preorder_traversal(root.right)
    return res

def postorder_traversal(root):
    res = []
    if root:
        res = res + postorder_traversal(root.left)
        res = res + postorder_traversal(root.right)
        res.append(root.val)
    return res

def run_tests():
    #      1
    #     / \
    #    2   3
    #   / \
    #  4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    assert inorder_traversal(root) == [4, 2, 5, 1, 3]
    assert preorder_traversal(root) == [1, 2, 4, 5, 3]
    assert postorder_traversal(root) == [4, 5, 2, 3, 1]
    
    print("[PASS] Binary Tree traversals")

if __name__ == "__main__":
    run_tests()
