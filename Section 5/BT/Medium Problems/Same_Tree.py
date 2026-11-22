# Brute Force
# Find the preorder sequence for both the trees and compare the sequences 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def preorder_traversal(self, root, result):
        if(root is None):
            result.append(None)
            return result
        result.append(root.val)
        self.preorder_traversal(root.left, result)
        self.preorder_traversla(root.right, result)
        
        return result
    def Same_Tree(self, p, q):
        arr1 = []
        arr2 = []
        tree_1 = self.preorder_traversal(p, arr1)
        tree_2 = self.preorder_traversal(q, arr2)
        return tree_1 == tree_2
    
    
# Optimal Solution 
# By utilizing short circuiting

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def preorder_traversal(self, root1, root2):
        if(root1 == None or root2 == None):
            return root1 == root2
        return (root1.val == root2.val) and self.preorder_traversal(root1.left, root2.left) and self.preorder_traversal(root1.right, root2.right)
    
    
         
        