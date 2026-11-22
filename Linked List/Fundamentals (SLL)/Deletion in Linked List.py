class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    # Deletion from head 
    def deletion_1(self):
        if(self.head == None):
            return
        current = self.head
        if(current.next == None):
            self.head = None
            return 
        self.head = current.next
        current = None
        return 
    # Deletion from the tail
    def deletion_2(self):
        if(self.head == None):
            return
        current = self.head
        # The head was the only element in the SLL and it was the tail 
        if(current.next == None):
            self.head = None
            return 
        while(current.next.next is not None):
            current = current.next
        current.next = None
        return 
    # Deletion from kth element of the LinkedList
    def deletion_3(self, k:int):
        if(self.head == None):
            return
        current = self.head
        if(current.next == None):
            self.head = None
            return
        position = 1
        while(position != k - 1):
            current = current.next
            position += 1
        current.next = current.next.next
        return 
    # Deletion of the element with value K 
    def deletion_4(self, value:int):
        if(self.head == None):  
            return 
        current = self.head
        if(current.next == None):
            self.head = None
            return
        if(current.data == value):
            self.head = current.next
            return 
        
        while(current.next.data != value):
            current = current.next
        current.next = current.next.next
        return 
        

        
  
  
