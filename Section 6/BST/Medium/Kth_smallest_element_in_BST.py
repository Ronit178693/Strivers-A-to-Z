# Brute Force 
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def dfs_traversal(self, root:Node, ans:list):
        if(root is None):
            return ans
        
        ans.append(root.val)
        self.dfs_traversal(root.left, ans)
        self.dfs_traversal(root.right, ans)
        
        return ans
    def Kth_smallest(self, root:Node, k:int):
        ans = []
        
        traversal = self.dfs_traversal(root, ans)
        traversal.sort()
        return traversal[k - 1]
'''
TC - O(N) + O(NLOGN)
SC - O(N)
'''

# Better Solution

# In-Order Traversal of a BST is always Sorted

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        
class Solution:
    def InOrder_Traversal(self, root:Node, ans:list):
        if(root is None):
            return ans 
        self.InOrder_Traversal(root.left, ans)
        ans.append(root)
        self.InOrder_Traversal(root.right, ans)
        return ans
    def smallest(self, root:Node, k:int):
        ans = []
                
        traversal = self.InOrder_Traversal(root, ans)
        return traversal[k - 1]
 

        