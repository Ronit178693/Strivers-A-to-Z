# Post Order Traversal using Recursion
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def Post_Traversal(self, root, result):
        if(root is None):
            return result
        self.Post_Traversal(root.left, result)
        self.Post_Traversal(root.right, result)
        result.append(root.data)
        return result
    def helper(self, root):
        result = []
        self.Post_Traversal(root, result)
        return result
    
# Post Order Traversal using Iteration
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def Post_Traversal(self, root):
        stack_2 = []
        if(root is None):
            return stack_2
        stack_1 = [root]
       
        while(stack_1):
            node = stack_1.pop()
            stack_2.append(node.val)
            if(node.left != None):
                stack_1.append(node.left)
            if(node.right != None):
                stack_1.append(node.right)
        return stack_2.reverse()