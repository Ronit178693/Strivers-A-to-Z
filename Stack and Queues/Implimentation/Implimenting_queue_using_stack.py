'''
We have to use 2 staks for this
let the queues be s1 and s2 
1) S1 -> S2
2) x -> S1
3) S2 -> S1
'''

# The push operation takes TC - O(2N) ans SC - O(2N) which is expensive so we cant use this when we have to push more and more elements 
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        # Step 1
        while(self.s1):
            self.s2.append(self.s1.pop())
            
        # Step 2
        self.s1.append(x)
        # Step 3
        while(self.s2):
            self.s1.append(self.s2.pop())
            
    def pop(self) -> int:
        if(len(self.s1) == 0):
            return 
        return self.s1.pop()
        
    def peek(self) -> int:
        return self.s1[len(self.s1) - 1]

    def empty(self) -> bool:
        if(len(self.s1) == 0):
            return True
        else:
            return False
        
# Approach where we have to push significantly more elements 
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        if(len(self.s2) != 0):
            return self.s2.pop()
        # There are no elements in s2
        else:
            while(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2.pop()
        
    def peek(self) -> int:
        if(len(self.s2) != 0):
            return self.s2[len(self.s2) - 1]
        else:
            # There are no elements in s2 then move all the elements from s1 down to s2
            while(self.s1):
                self.s2.append(self.s1.pop())
            return self.s2[len(self.s2) - 1]

    def empty(self) -> bool:
        if(len(self.s2) == 0 and len(self.s1) == 0):
            return True
        else:
            return False