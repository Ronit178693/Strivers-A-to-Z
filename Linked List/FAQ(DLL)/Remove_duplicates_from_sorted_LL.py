# Brute Force Solution 
class Node:
    def __init__(self, data):
        self.data = data
        self.next - None
        self.prev = None
class Solution:
    def remove_duplicates(self, head):
        hash = set()
        current = head
        # Makes the enty of the linkedlist in the hash 
        while(current is not None):
            if(current not in hash):
                hash.add(current)
        
            current = current.next
        set_to_list = list(hash.sort())
        return set_to_list[0]
    
# Better Solution 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Solution:
    def remove_duplicants(self, head):
        values = []
        current = head
        while(current is not None):
            values.append(current.data)
            duplicant_check = current.data
            while(current is not None and duplicant_check == current.data):
                current = current.next 
        newNode = Node(values[0])
        temp = newNode
        for i in values[1:]:
            dummyNode = Node(i)
            temp.next = dummyNode
            dummyNode.prev = temp
            temp = temp.next 
        temp.next = None
        return newNode
# Optimal Solution 
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class Solution:
    def remove_duplicants(self, head):
        if(head.next is None):
            return head
        current = head 
        duplicate = current.next
        while(current.next is not None):
           
            if(duplicate is not None and current.val == duplicate.val ):
                duplicate = duplicate.next
            else:
                current.next = duplicate
                if(duplicate is not None):
                    duplicate.prev = current
                    current = duplicate
                    duplicate = duplicate.next
        return head
                
                
            
            
            
            
        
        