class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.rigt = None
class Solution:
    # Find the path from node a and node b to the root and then compare the paths 
    def path_to_root(self, root:Node, x:Node, ds:list):
        if(root is None):
            return False
        if(root.val == x.val):
            return True
        left = self.path_to_root(root.left, x, ds)
        right = self.path_to_root(root.right, x, ds)
        if(left == True or right == True):
            return True
        else:
            ds.pop()
            return False
    def LCA(self, root:Node, q:Node, p:Node):
        ds1 = []
        ds2 = []
        q_path = self.path_to_root(root, q, ds1)
        q_path = ds1
        p_path = self.path_to_root(root, p, ds2)
        p_path = ds2
        
        for i in range(min(len(q_path), len(p_path))):
            if(q_path[i] != p_path[i]):
                return p_path[i - 1]
            
# Optimal Solution
class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.right = None
class Solution:
    def LCA(self, root:Node, p:Node, q:Node):
        if(root is None):
            return None
        if(root == p):
            return p
        elif(root == q):
            return q
        left = self.LCA(root.left, p, q)
        right = self.LCA(root.right, p, q)
        if(left is None and right is not None):
            return right
        elif(left is not None and right is None):
            return left
        elif(left is None and right is None):
            return None
        return root
            
        