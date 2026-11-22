class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def Max(self, root:Node):
        while(root.right is not None):
            root = root.right 
        return root
    def Min(self, root:Node):
        while (root.left is not None):
            root = root.left
        return root
            
    def both(self, root:Node):
        if(root is None):
            return []
        maxx = self.Max(root)
        minn = self.Min(root)
        return [maxx, minn]