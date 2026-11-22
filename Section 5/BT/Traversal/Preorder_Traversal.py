#  Recursive Approach
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def preorder_traversal(self, root, result):
        if(root is None):
            return result
        result.append(root.data)
        self.preorder_traversal(root.left, result)
        self.preorder_traversal(root.right, result)
        return result
    def helper(self, root):
        result = []
        self.preorder_traversal(root, result)
        return result
    
# Iterative Approach
        
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def preorder_traversal(self, root):
        result = []
        if(root == None):
            return result
        stack = [root]
        while(stack == True):
            node = stack.pop()
            result.appen(node.val)
            if(node.right != None):
                stack.append(node.rignt)        
            if(node.left != None):
                stack.append(node.left) 
        return result