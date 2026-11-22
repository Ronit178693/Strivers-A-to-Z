class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DLL:
    def __init__(self):
        self.head = None
    def Insertion_1(self, data):
        if(self.head == None):
            newNode = Node(data)
            return 
        current = self.head
        newNode = Node(data)
        newNode.next = current
        current.prev = newNode
        self.head = current.prev
        return 
    # Instertion after tail
    def Insertion_2(self, data):
        if(self.head == None):
            newNode = Node(data)
            return 
        current = self.head
        while(current.next is not None):
            current = current.next
        newNode = Node(data)
        current.next = newNode
        newNode.prev = current
    # Insert at a 1-based position; position len(list) + 1 appends.
    def Insertion_3(self, position, data):
        newNode = Node(data)
        if position == 1:
            newNode.next = self.head
            if self.head is not None:
                self.head.prev = newNode
            self.head = newNode
            return

        current = self.head

        newNode.prev = current
        newNode.next = current.next
        if current.next is not None:
            current.next.prev = newNode
        current.next = newNode

    # Insert before the first node whose value matches value.
    def Insertion_4(self, data, value):
        current = self.head
        while current is not None and current.data != value:
            current = current.next
        newNode = Node(data)
        newNode.next = current
        newNode.prev = current.prev
        if current.prev is None:
            self.head = newNode
        else:
            current.prev.next = newNode
        current.prev = newNode
            

