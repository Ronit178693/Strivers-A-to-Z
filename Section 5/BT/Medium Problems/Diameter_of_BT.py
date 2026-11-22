# Brute Force 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        # Global variable to
        # store the diameter
        self.diameter = 0  

    def height(self, root):
        if(root == None):
            return 0
        # To find the height of a half we use the formular 1 + max(lh+rh)
        lh = self.height(root.left)
        rh = self.height(root.right)
        
        self.diameter = max(self.diameter, lh+rh)
        
        return 1+max(lh,rh)
    def Diameter(self, root):
        
        self.height(root)
        return self.diameter
        