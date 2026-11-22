''' 
Solving this problem uses two-tier recursive strategy.
1) Pop all the elements using recursion 
2) Once the stack is empty, start pushing the elements back in the stack 
3) push 1, stack become [1]
4) push 2, pop 1 first, append 2 then again append 1 so the stack becomes [2,1]
5) push 3, pop 2 and 1, append 3then again append 2 and 1 so the stack becomes [3, 2, 1]
'''

def stack(st:list):
    
