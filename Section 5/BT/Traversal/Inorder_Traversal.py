# InOrder Traversal Using Recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def Inorder_Traversal(self, root, result):
        if(root is None):
            return result
        self.Inorder_Traversal(root.left, result)
        result.append(root.data)
        self.Inorder_Traversal(root.right, result)
        return result

    def helper(self, root):
        result = []
        self.Inorder_Traversal(root, result)
        return result  
    
#   InOrder Traversal Using Iteration

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    
    def InOrder_Traversal(self, root):
        result = []
       
        if(root == None):
            return result
        node = root
        stack = []
        while(True):
            if(node != None):
                stack.append(node)
                node = node.left 
            else:
                if(not stack):
                    break
                node = stack.pop()
                result.append(node.val)
                node = node.right
        return result
                
                
            
