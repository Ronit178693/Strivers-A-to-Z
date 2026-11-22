class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def valid_BST(self, root:Node, MIN = float('-inf'), MAX = float('inf')):
        if(root is None):
            return True
        # Checking this for every root if the root value goes out of boundaries then the tree is not a BST
        if(root.val > MAX or root.val < MIN):
            return False
        return (self.valid_BST(root.left, MIN, root.val) and self.valid_BST(root.right, root.val, MAX))
        