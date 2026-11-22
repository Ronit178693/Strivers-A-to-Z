# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def helper(self, root, result):
        if(root is None):
            return 
        self.helper(root.left, result)
        result.append(root)
        self.helper(root.right, result)
        return result

    def recoverTree(self, root: TreeNode | None) -> None:
        inorder = self.helper(root, [])
        # Sorting the inorder on the basis of the node values 
        # Now we have the valid BST inorder 
        # As the inorder for a valid BST is always sorted 
        correct_inorder = sorted(node.val for node in inorder)

        for i in range(len(inorder)):
            inorder[i].val = correct_inorder[i]




        