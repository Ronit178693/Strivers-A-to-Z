from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hashing(self, root):
        if(root is None):
            return 
        # Storing the root node in the queue
        queue = deque()
        queue.append(root)
        # Initializing a hash to store all the parent nodes 
        hashi = {root: None}
        # Populates the hash with all the parent child pairs
        while(queue):
            for i in range(len(queue)):
                node = queue.popleft()
                if(node.left):
                    queue.append(node.left)
                    hashi[node.left] = node
                if(node.right):
                    queue.append(node.right)
                    hashi[node.right] = node
        return hashi
        # Traversing to the target node 
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        if(root is None):
            return 
        # Initializing the queue and the visited DS with the target
        seen = {target}
        queue = deque()
        queue.append(target)
        distance = 0
        # Initializing hashing function here
        parents = self.hashing(root)
        while(queue):
            if(distance == k):
                break
            for i in range(len(queue)):
                node = queue.popleft()
                
                if(node.right is not None and node.right not in seen):
                    seen.add(node.right)
                    queue.append(node.right)
                if(node.left and node.left not in seen):
                    seen.add(node.left)
                    queue.append(node.left)
                if(parents[node] is not None and parents[node] not in seen):
                    seen.add(parents[node])
                    queue.append(parents[node])
            distance += 1
            
            
        return [
            node.val
            for node in queue
        ]
        