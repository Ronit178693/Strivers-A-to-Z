class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
class Solution:
    def BT(self, InOrder:list, PostOrder:list):
        if(len(InOrder) == 0 or len(PostOrder) == 0):
            return None
        root_val = PostOrder[len(PostOrder) - 1]
        # Finds the index of root inside InOrder Sequence
        for i in range(len(InOrder)):
            if(root_val == InOrder[i]):
                root_indx = i
        left_InOrder = InOrder[:root_indx]
        right_InOrder = InOrder[root_indx + 1:]
        left_PostOrder =  PostOrder[:len(left_InOrder)]
        right_PostOrder = PostOrder[len(left_PostOrder):len(PostOrder) - 1]
        
        root = Node(root_val)
        
        root.right = self.buildTree(right_InOrder, right_PostOrder)
        root.left = self.buildTree(left_InOrder, left_PostOrder)
        
        return root
        