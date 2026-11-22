# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def bstFromPreorder(self, preorder: list[int]) -> TreeNode | None:
        if(len(preorder) == 0):
            return None
            # The first node of the array will be the root node of the tree
        root_node = preorder[0]
        i = 1
        while(i < len(preorder) and preorder[i] < root_node):
            i += 1
        preorder_left = preorder[1:i]
        preorder_right = preorder[i:]
        root = TreeNode(root_node)
        root.left = self.bstFromPreorder(preorder_left)
        root.right = self.bstFromPreorder(preorder_right)
        return root

        