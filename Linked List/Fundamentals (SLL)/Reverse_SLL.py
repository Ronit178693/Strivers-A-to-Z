class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
class SLL:
    def __init__ (self):
        self.next = None
    def reverse(self):
        # Case 1) If the SLL is empty
        if(self.head is None):
            return
        # Case 2) If SSL only got 1 element 
        if(self.head.next == None):
            return self.head
        # If more the 1 elements then reverse the links
        current = self.head 
        prev = None
        while(current is not None):
            temp = current.next
            current.next = prev
            prev = current
            
            current = temp