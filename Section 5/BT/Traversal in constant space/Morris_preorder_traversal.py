'''
Takes O(N) TC for traversal but takes O(1) SC 
using the concept of threaded BT
'''
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

class Solution:
    def Morris_preorder(self, root):
        # For returning the answer
        result = []
        current = root
         
        while(current):
            # If the tree dont have any left subtree then just print the root and move right 
            if(current.left is None):
                result.append(current.val)
                current = current.right
            else:
                # Pointing to the root node of the left subtree 
                curr_left = current.left
                while(curr_left.right and curr_left.right != current):
                    curr_left = curr_left.right
                # Once we have reached to the right most node in the left subtree 
                if(curr_left.right == None):
                    curr_left.right = current
                    result.append(current.val)
                    current = current.left
                # If the link thread already existed then remove the thread and move right 
                else:
                    curr_left.right = None
                    
                    current = current.right
        return result