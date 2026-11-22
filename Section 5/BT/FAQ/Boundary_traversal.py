class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def leaf_checker(self, root:list):
        # Checking if the the node is root node 
        return not root.left and not root.right
    
    def left_subtree_traversal(self, root:list, ds:list):

        while(True):
            if(self.leaf_checker(root) == False):
                ds.append(root)
            else:
                break
            if(root.left != None):
                root = root.left
            else:
                root = root.right
        

    def right_subtree_traversal_in_reverse(self, root:list, ds:list, st:list):
        while(True):
            if(self.leaf_checker(root) == False):
                st.append(root)
            else:
                break
            if(root.right != None):
                root = root.right
            else:
                root = root.left
        
        for i in st:
            node = st.pop()
            ds.append(node)
            
            
  
    def pre_order_traversal_leafs(self, root:list, ds:list):
        
        if(self.leaf_checker == True):
            ds.append(root)
            return 
            
        if(root.left != None):
            self.pre_order_traversal_leafs(root.left, ds)
        if(root.right != None):
            self.pre_order_traversal_leafs(root.right, ds)
            
        
            
            
    def Boundary_traversal(self, root:list):
        ds = []
        if(root is None):
            return ds 
        ds.append(root.val)
        if(self.leaf_checker(root) == True):
            return ds
        st = []
        self.left_subtree_traversal(root.left, ds)
        self.pre_order_traversal_leafs(root, ds)
        self.right_subtree_traversal_in_reverse(root.right, ds, st)
        
        
                