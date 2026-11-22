class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
class Solution:
    def clone(self, head):
        if(head is None):
            return head
        # Stores original Node : dummynode
        hash = {}
        dummyNode = Node(0)
        temp = dummyNode
        current = head
        # This loop is for populating the hash and forming the new linkedlist with the values and next pointers set 
        while(current is not None):
            cloneNode = Node(current.data)
            hash[current] = cloneNode
            temp.next = cloneNode
            temp = temp.next
        # Now searching from the hash map and mapping the random pointers 
        current = head
        while(current is not None):
            clone_Node = hash[current]
            if(current.random is not None):
                clone_Node.random = hash[current.random]
            else:
                clone_Node.random = None
        return dummyNode.next

# Optimal Solution 
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None
class LinkedList:
    def instert(self, head):
        current = head 
        temp = head
        while(temp is not None):
            newNode = Node(temp.data)
            temp = temp.next
            current.next = newNode
            current = current.next
            current.next = temp
            current = current.next
        return head 
    def random(self, head):
        current = head
        while(current is not None):
            if(current.random is not None):
                current.next.random = current.random.next
            else:
                current.next.random = None
            current = current.next.next
        return head 
    def next(self, head):
        dummyNode = Node(-1)
        temp = dummyNode
        current = head 
        while(current is not None):
            clone = current.next
            temp.next = clone
            temp = temp.next
            
            current.next = clone.next
            current = current.next
        return dummyNode.next
    def final(self, head):
        dummy_inserted_LL = self.instert(head)
        random_pointer_ll = self.random(dummy_inserted_LL)
        final_ll = self.next(random_pointer_ll)
        return final_ll
        
            
            
                
            