class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class solution:
    def __init__(self):
        # Dummy starting node
        self.head = Node(-1)
        self.tail = self.head

    def empty(self) -> bool:
        # If hter is nothing in the LL then return None
        if(self.head.next == None):
            return True
        return False
    def push(self, x):
        newNode = Node(x)
        self.tail.next = newNode
        self.tail = newNode
    def pop(self):
        if(self.head.next == None):
            return -1
        self.head.next = self.head.next.next
        if(self.head.next == None):
            self.tail = self.head
    def peek(self):
        if(self.head.next == None):
            return -1
        return self.head.next.data
