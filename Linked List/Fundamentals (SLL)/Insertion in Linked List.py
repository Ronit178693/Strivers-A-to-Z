class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    # Insert at head
    def Insertion_1(self, data:int):
        newNode = Node(data)
        # No element in the LinkedList
        if(self.head == None):
            self.head = newNode
            return 
        newNode.next = self.head
        self.head = newNode
        return 
    # Insertion at end
    def Insertion_2(self, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            return 
        current = self.head
        while(current is not None):
            current = current.next
        current.next = newNode
        return 
    # Insertion at kth position 
    def Insertion_3(self, position, data):
        newNode = Node(data)
        if(self.head == None):
            self.head = newNode
            return 
        i = 1
        while(i != position - 1):
            current = current.next 
        newNode.next = current.next
        current.next = newNode
        return 
    # Insert before the value in the LinkedList
    def Insertion_4(self, data, value):
        newNode = Node(data)
        if(self.head is None):
            newNode = self.head
            return 
        current = self.head 
        
        while(current.next.data != value):
            cureent = current.next
        newNode.next = current.next
        current.next = newNode
        return 
            