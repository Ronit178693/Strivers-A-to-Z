class MyStack:
    # Going to impliment queue using lists 
    def __init__(self):
        self.queue = []
        
    def push(self, x: int) -> None:
        self.queue.append(x)
        for i in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))
    
    def pop(self) -> int:
        if(len(self.queue) == 0):
            return -1
        return self.queue.pop(0)

    def top(self) -> int:
        if(len(self.queue) == 0):
            return -1
        return self.queue[0]

    def empty(self) -> bool:
        if(len(self.queue) == 0):
            return True 
        return False


