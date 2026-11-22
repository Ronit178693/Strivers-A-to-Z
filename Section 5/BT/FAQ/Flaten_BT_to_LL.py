# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorder_traversal(self, root, result):
        if(root is None):
            return 
        result.append(root)
        self.preorder_traversal(root.left, result)
        self.preorder_traversal(root.right, result)

        return result
    def flatten(self, root: TreeNode | None) -> None:
        if(root is None):
            return 
        result = []
        # Stores the order of the nodes
        order = self.preorder_traversal(root, result)
        dummyNode = TreeNode(-1)
        current = dummyNode
        for i in order:
            current.right = i
            current.left = None
            current = current.right
        dummyNode = dummyNode.right
        dummyNode.left = None
        