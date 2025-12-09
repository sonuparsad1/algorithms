"""
Title: AVL Tree (Balanced BST)
Topic: Data Structures

Theory:
    Self-balancing BST.
    Balance Factor = Height(Left) - Height(Right).
    Allowed BF: {-1, 0, 1}.
    
    Rotations: Left, Right, Left-Right, Right-Left.
    
    Complexity: O(log n) for insert/delete/search.
"""

class AVLNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, root):
        if not root: return 0
        return root.height

    def get_balance(self, root):
        if not root: return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        
        x.right = y
        y.left = T2
        
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        
        y.left = x
        x.right = T2
        
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key):
        if not root:
            return AVLNode(key)
        
        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
            
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        
        balance = self.get_balance(root)
        
        # Left Left
        if balance > 1 and key < root.left.val:
            return self.right_rotate(root)
            
        # Right Right
        if balance < -1 and key > root.right.val:
            return self.left_rotate(root)
            
        # Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
            
        # Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)
            
        return root

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.val)
            res = res + self.inorder(root.right)
        return res

def run_tests():
    tree = AVLTree()
    root = None
    
    # Inserting in sorted order would skew a normal BST (O(n))
    # AVL should balance it (O(log n))
    keys = [10, 20, 30, 40, 50, 25]
    for k in keys:
        root = tree.insert(root, k)
        
    # Preorder check for structure would be better, but inorder checks BST property
    inorder = tree.inorder(root)
    assert inorder == sorted(keys)
    
    # Check balance (Root should be 30 for this specific insertion set?)
    # 10, 20, 30, 40, 50, 25
    #      30
    #     /  \
    #    20  40
    #   /  \   \
    #  10  25  50
    assert root.val == 30 
    
    print("[PASS] AVL Tree insertion and balancing")

if __name__ == "__main__":
    run_tests()
