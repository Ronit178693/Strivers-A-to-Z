class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node in the queue

class LinkedListQueue:
    def __init__(self):
        self.front = None  # Points to the first element to be removed
        self.rear = None   # Points to the last element added
        self.current_size = 0

    def is_empty(self) -> bool:
        return self.front is None

    def enqueue(self, item) -> None:
        new_node = Node(item)
        
        # If queue is empty, both front and rear point to the new node
        if self.is_empty():
            self.front = new_node
            self.rear = new_node
        else:
            # Link the old rear node to the new node
            self.rear.next = new_node
            # Advance the rear pointer to the new node
            self.rear = new_node
            
        self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        
        # Extract data from the front node
        dequeued_item = self.front.data
        # Move the front pointer forward to the next node
        self.front = self.front.next
        
        # If front becomes None, the queue is now empty, so reset rear as well
        if self.front is None:
            self.rear = None
            
        self.current_size -= 1
        return dequeued_item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.front.data

    def size(self) -> int:
        return self.current_size
