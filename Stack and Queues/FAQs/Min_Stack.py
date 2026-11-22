class MinStack:

    def __init__(self):
        self.stack = []
        self.pair = []

    def push(self, value: int) -> None:
        # If the stack is empty we just insert the first element and the min is also the first element
        if(len(self.stack) == 0):
            self.stack.append((value, value))
        # If there are already elements present in stack 
        else:
            self.stack.append((value, min(value, self.stack[-1][1])))
    def pop(self) -> None:
        if(len(self.stack) == 0):
            return -1
        else:
            return self.stack.pop()
    def top(self) -> int:
        if(len(self.stack) == 0):
            return -1
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        if(len(self.stack) == 0):
            return -1
        return self.stack[-1][1]