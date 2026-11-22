# Brute Force solution taking O(N) for the iteration and O(N) in worst case for the second function, SC - O(3N)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None
        
class Solution:
    def iteration(self, root, result):
        if(root is None):
            return
        self.iteration(root.left, result)
        result.append(root.val)
        self.iteration(root.right, result)
        
        return result
    
    def sum(self, root, k):
        inorder = self.iteration( root, [])
        i, j = 0, len(inorder) - 1
        while(i < j):
            sum = inorder[i] + inorder[j]
            if(sum == k):
                return True
            if(sum > k):
                j -= 1
            elif(sum < k):
                i += 1
        return False
    
