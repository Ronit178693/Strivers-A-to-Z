class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.rigt = None
class Solution:
    def helper(self, root:Node, ds:list, node):
        if(root is None):
            return False
        ds.append(root.val)
        if(root.val == node):
            return True
       
        left = self.helper(root.left, ds, node)
        right = self.helper(root.right, ds, node)
        if(right == True or left == True):
            return True
        ds.pop()
        return False
    def path(self, root:Node, node):
        ds = []
        # Call Helper for the final list
        self.helper(root, ds, node)
        return ds