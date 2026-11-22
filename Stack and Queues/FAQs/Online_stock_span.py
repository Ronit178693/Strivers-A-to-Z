# Brute Force solution using O(N) TC for rvery element 
class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)
        span, i = 1, len(self.stack) - 1
        j = i - 1
        while(j >= 0):
            if(self.stack[i] >= self.stack[j]):
                span += 1
                j -= 1
            else:
                break
        return span

# Better Solution using PGE 

class StockSpanner:

    def __init__(self):
        self.stack = []
        self.prices = []
        self.index = 0
    

    def next(self, price: int) -> int:
        self.prices.append(price)
        # We dont need a for loop here as we are insterting the elements in the array one by one
        while(self.stack and self.prices[self.stack[-1]] <= price):
            self.stack.pop()

        if(not self.stack):
            span = self.index + 1
        else:
            span = self.index - self.stack[-1]
        self.stack.append(self.index)
        self.index += 1
        return span
        



