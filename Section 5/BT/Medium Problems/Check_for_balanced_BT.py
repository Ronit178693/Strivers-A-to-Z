#  Brute Force
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def height(self, root:list):
        if(root is None):
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        
        return 1 + max(left, right)
    def isBalanced(self, root:list):
        if(root is None):
            return True

        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if abs(left - right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True 
        return False
    
# Optimal Solution 
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def height(self, root:list):
           
        if(root is None):
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        if(left == -1 or right == -1):
            return -1
        if(abs(left - right) <= 1):
            return 1 + max(left, right)
        else:
            return -1

    def isBalanced(self, root:list):
        # Returns true if the function returns anything except -1
        return self.height(root) != -1
        
                
            
            