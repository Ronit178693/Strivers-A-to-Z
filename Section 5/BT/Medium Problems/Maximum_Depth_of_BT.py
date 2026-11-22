class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def Maximum(self, root:list):
        if(root == None):
            return 0
        left = self.Maximum(root.left)
        right = self.Maximum(root.right)
        
        return 1+max(left, right)