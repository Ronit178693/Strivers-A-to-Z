class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.sum = 0
    def Maximum_Sum(self, root):
        if(root != None):
            return 0
        lh = max(0,self.Maximum_Sum(root.left))
        rh = max(0,self.Maximum_Sum(root.right))
        
        self.sum = max(self.sum, lh+rh+root.data)
        return (root.data + max(lh, rh))
    def maxPathSum(self, root):
        self.Maximum_Sum(root)
        return self.sum