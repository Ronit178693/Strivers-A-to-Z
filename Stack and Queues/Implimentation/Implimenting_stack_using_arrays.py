# Stack implimented using arrays (traditional stack implimentation by predefining an array in memeory)
class BoundedStack:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Pre-allocate a fixed-size array in memory
        self.stack = [None] * capacity  
        self.top = -1  # Pointer to the current top element
    def is_empty(self) -> bool:
        return self.top == -1

    def is_full(self) -> bool:
        return self.top == self.capacity - 1

    def push(self, item) -> None:
        if self.is_full():
            raise OverflowError("Stack Overflow: Cannot push to a full stack.")
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        item = self.stack[self.top]
        self.stack[self.top] = None  # Clear memory reference
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack[self.top]

    def size(self) -> int:
        return self.top + 1


# Stack implimented using arrays (stack being implimented by using pythons dynamic lists)

class DynamicStack:
    def __init__(self):
        self.stack = []  # Dynamic array

    def is_empty(self) -> bool:
        return len(self.stack) == 0

    def push(self, item) -> None:
        self.stack.append(item)  # O(1) amortised time

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Cannot pop from an empty stack.")
        return self.stack.pop()  # O(1) time

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty.")
        return self.stack[-1]  # Read the last element

    def size(self) -> int:
        return len(self.stack)
