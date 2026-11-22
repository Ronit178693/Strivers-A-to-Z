# Brute Force Solution - Generating the inorder sequence and then finding the successor 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def inorder(self, root, result):
        if(root is None):
            return 
        self.inorder(root.left, result)
        result.append(root)
        self.inorder(root.right, result)
        return result
    def successor(self, root, k):
        # Gives the inorder sequence
        result = self.inorder(root,  [])
        for i in range(len(result)):
            if(result[i] == k):
                # If we have found the key befor the ending of the array then return the next element 
                if(i < len(result) - 1):
                    return result[i + 1]
                else:
                    # If the element is not found or is found at the end then return -1 
                    return -1 
        return -1
    
    
# Better solution using Morris Traversal 

# Optimal solution 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    
    def successor(self, root, k):
        if(root is None):
            return 
        successor = None
        while(root):
            if(root.val > k):
                # Move to the left 
                successor = root.val
                root = root.left 
            else:
                root = root.right
        return successor
'''
TC - O(h), h - Height of the tree, SC - O(1)
'''

    