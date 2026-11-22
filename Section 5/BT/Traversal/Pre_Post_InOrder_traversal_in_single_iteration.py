class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def All_in_One(self, root):
        InOrder = []
        PreOrder = []
        PostOrder = []
        stack = [(root, 1)]
        if(root == None):
            return []
        while(stack):
            node, state = stack.pop()
            if(state == 1):
                PreOrder.append(node.data)
                stack.append((node, 2))
                if(node.left):
                    stack.append((node.left, 1))
            elif(state == 2):
                InOrder.append(node.data)
                stack.append((node, 2))
                if(node.right):
                    stack.append((node.right, 1))
            else:
                PostOrder.append(node.data)
        return [PreOrder, PostOrder, InOrder]
    