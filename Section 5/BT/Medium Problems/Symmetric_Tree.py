class Node:
    def __init__(self, val):
        self.val = self.val
        self.left = None
        self.right = None
class Solution:
    def helper(self, root1, root2):
        if(root1 is None and root2 is not None or root1 is not None and root2 is None):
            return False
        if(root1 is None and root2 is None):
            return True
        if(root1.val != root2.val):
            return False
        sec1 = self.helper(root1.left, root2.right)
        sec2 = self.helper(root1.right, root2.left)
        return sec1 and sec2
    def symmetric(self, root):
        if(root is None):
            return True
        return self.helper(root.left, root.right)
        
        
        