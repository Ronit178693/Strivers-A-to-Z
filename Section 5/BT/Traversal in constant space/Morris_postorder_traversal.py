from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        curr = root
        
        while curr:
            # If there is no right child, process current node and move left
            if not curr.right:
                res.append(curr.val)
                curr = curr.left
            else:
                # Find the leftmost node in the right subtree (successor)
                successor = curr.right
                while successor.left and successor.left != curr:
                    successor = successor.left
                
                # If the temporary link doesn't exist, create it
                if not successor.left:
                    res.append(curr.val) # Process Root before going Right
                    successor.left = curr
                    curr = curr.right
                # If the link already exists, break it to restore the tree structure
                else:
                    successor.left = None
                    curr = curr.left
                    
        # Reverse the entire result to convert Root->Right->Left into Left->Right->Root
        return res[::-1]
