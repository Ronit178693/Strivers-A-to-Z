'''
When you implement a strict linear queue with a fixed-size array, you face a major dilemma called false overflow: once your rear pointer reaches the end of the array, you cannot insert any more items, even if you have popped elements and the front of the array is completely empty.
'''
# Implimenting Queue using array (Using circular queues)
class CircularQueue:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.queue = [None] * capacity  # Pre-allocated fixed array
        self.front = -1
        self.rear = -1
        self.current_size = 0

    def is_empty(self) -> bool:
        return self.current_size == 0

    def is_full(self) -> bool:
        return self.current_size == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            raise OverflowError("Queue Overflow: Cannot enqueue to a full queue.")
        if(self.current_size == 0):
            self.front, self.end = 0, 0
        else:
            self.rear = (self.rear + 1) % self.capacity 
        self.queue[self.rear] = item
        # Circular wrap-around using modulo arithmetic
        self.current_size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        item = self.queue[self.front]
        self.queue[self.front] = None  # Clear memory reference
                # Circular wrap-around using modulo arithmetic
        if(self.current_size == 1):
            self.front, self.rear = -1, -1
        else:
            self.front = (self.front + 1) % self.capacity  
       
        self.current_size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[self.front]

    def size(self) -> int:
        return self.current_size


# # Implimenting Queue using array (Using pythons list)
class DynamicQueue:
    def __init__(self):
        self.queue = []  # Dynamic array

    def is_empty(self) -> bool:
        return len(self.queue) == 0

    def enqueue(self, item) -> None:
        self.queue.append(item)  # O(1) amortised time

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Cannot dequeue from an empty queue.")
        # WARNING: This triggers an O(n) element shift operation in Python memory
        return self.queue.pop(0)  

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty.")
        return self.queue[0]

    def size(self) -> int:
        return len(self.queue)
