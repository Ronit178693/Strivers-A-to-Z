class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
# Brute force solution taking O(N) TC via any traversal 
class Solution:
    def count_nodes(self, root):
        if(root is None):
            return 0
        left_count = self.count_nodes(root)
        right_count = self.count_nodes(root)
        
        return 1 + left_count + right_count
    

class Solution:
    # Calculating the left height of the tree going down only one branch
    def calculate_left(self, root):
        if(root is None):
            return 0
        left = self.calculate_left(root.left)
        return 1 + left
    
    # Calculating the right height of the tree going down only one branch
    def calculate_right(self, root):
        if(root is None):
            return 0
        right = self.calculate_right(root.right)
        return 1 + right
    
    def count_nodes(self, root):
        if(root is None):
            return 0
        lh = self.calculate_left(root)
        rh = self.calculate_right(root)
        if(lh == rh):
            return ((2**lh) - 1)
        left = self.count_node(root.left)
        right = self.count_node(root.right)
        
        return 1 + left + right