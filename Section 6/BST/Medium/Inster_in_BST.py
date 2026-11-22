class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def Instert(self, root:TreeNode, val:TreeNode):
        if(root is None):
            return TreeNode(val)
        current = root # making a copy of root to make changes in it as returning the tree in response needs the root element 
        #  Going to make changes in place 
        while(True):
            if(current.val > val):
                #  Move left 
                if(current.left is None):
                    current.left = TreeNode(val)
                    break
                current = current.left
            else:
                if(current.right is None):
                    current.right = TreeNode(val)
                    break
                current = current.right
        return root