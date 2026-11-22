# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.nodes = []
        self.indx = 0
        # Populating the nodes array
        self.inorder(root)

    def inorder(self,root):
        if(root is None):
            return 
        self.inorder(root.left)
        self.nodes.append(root)
        self.inorder(root.right)
      
    def next(self) -> int:
        value = self.nodes[self.indx]
        self.indx += 1
        return value.val

    def hasNext(self) -> bool:
        return self.indx < len(self.nodes)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()



# Optimal Solution taking SC - O(H) H = Height of the tree 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode | None):
        self.stack = []
        self.inorder(root)
    def inorder(self, root):
        while(root is not None):
            self.stack.append(root)
            root = root.left
        # All the left node values are in stack now move right 
    def next(self) -> int:
        node = self.stack.pop()
        if(node.right):
            right_child = node.right
            self.inorder(right_child)
        return node.val
    def hasNext(self) -> bool:
        if(len(self.stack) == 0):
            return False
        return True
# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()