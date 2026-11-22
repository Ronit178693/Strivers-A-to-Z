class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def LCA(self, root:Node, p:Node, q:Node):
        if(root is None):
            return None
        if(p.val > root.val and q.val > root.val):
            return self.LCA(root.right, p, q)
        if(p.val < root.val and q.val < root.val):
            return self.LCA(root.left, p, q)
        # return the root if both of them lyes on opposite sides
        return root