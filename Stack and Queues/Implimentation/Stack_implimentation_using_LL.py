class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node down in the stack

class LinkedListStack:
    def __init__(self):
        self.top = None  # Head of the linked list
        self.current_size = 0

    def is_empty(self) -> bool:
        return self.top is None

    def push(self, item) -> None:
        new_node = Node(item)
        # Point the new node to the current top element
        new_node.next = self.top
        # Reassign top to our new node
        self.top = new_node
        self.current_size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        
        # Extract data from the top node
        popped_item = self.top.data
        # Advance the top pointer to the next node down
        self.top = self.top.next
        self.current_size -= 1
        
        return popped_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.top.data

    def size(self) -> int:
        return self.current_size
