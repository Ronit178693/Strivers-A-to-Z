# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root):
        if(root.right is None):
            return root.left
        elif(root.left is None):
            return root.right
        # If both are present 
        right_child, left_child = root.right, root.left
        # Move to the extreme right of the left child
        while(left_child.right is not None):
            left_child = left_child.right
        left_child.right = right_child
        return root.left
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        if(root is None):
            return root 
        if(root.val == key):
            return self.helper(root)
        # If we have to delete the root node 
        current = root 
        while(root is not None):
            if(root.val > key):
                # Move left
                if(root.left and root.left.val == key):
                    root.left = self.helper(root.left)
                    # Once we have deleted our node break out of the loop 
                    break
                else:
                    root = root.left
            else:
                # Move right
                if(root.right and root.right.val == key):
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return current 

        