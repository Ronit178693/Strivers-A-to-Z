class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
    # Deletion of the head 
    def deletion_1(self):
        # The linkedlist is empty
        if(self.head == None):
            return 
        # The linkedlist had only single element
        if(self.head.next == None):
            self.head = None
            return 
        # Having more elements
        current = self.head
        self.head = current.next
        self.head.prev = None
        return 
    # Deletion from the tail of DLL 
    def deletion_2(self):
        # The linkedlist is empty
        if(self.head == None):
            return 
        # The linkedlist had only single element
        if(self.head.next == None):
            self.head = None
            return 
        current = self.head 
        while(current.next.next is not None):
            current = current.next
        current.next.prev = None
        current.next = None
        return 
    # Delete Kth element of DLL 
    def deletion_3(self, k:int):
        # The linkedlist is empty
        if(self.head == None ):
            return 
        # The linkedlist had only single element
        if(self.head.next == None):
            self.head = None
            return 
        if(k == 1):
            self.head = self.head.next
            self.prev.next = None
            self.prev = None
            
        current = self.head
        position = 1
        while(current is not None and position != k):
            current = current.next
        current.prev.next = current.next
        current.next.prev = current.prev
        current = None
    # Deleting a certain node in DLL 
    def deletion_4(self, value):
        # The linkedlist is empty
        if(self.head == None ):
            return 
        # The linkedlist had only single element
        if(self.head.next == None):
            self.head = None
            return 
        while(current.data != value):
            current = current.next
        
        
        
        