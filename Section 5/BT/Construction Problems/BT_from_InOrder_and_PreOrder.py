class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def BT(self, InOrder:list, PreOrder:list):
        if len(InOrder) == 0 or len(PreOrder) == 0:
            return None
        root_val = PreOrder[0]
        for i in range(len(InOrder)):
            if(root_val == InOrder[i]):
                root_indx = i
        left_InOrder = InOrder[:root_indx]
        right_InOrder = InOrder[root_indx + 1:]
        left_PreOrder = PreOrder[1:len(left_InOrder) + 1]
        right_PreOrder = PreOrder[len(left_PreOrder) + 1:]
        # Creating the root node
        root = Node(root_val)
    
        root.left = self.buildTree(left_PreOrder, left_InOrder)
        root.right = self.buildTree(right_PreOrder, right_InOrder)
        
        return root
        
        
            