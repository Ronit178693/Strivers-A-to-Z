# Optimal Solution
'''
Instead of generating invalid paths and discarding them later, you place guards at the entrance of your recursive choices. You keep a running count of how many opening parentheses (open_p) and closing parentheses (close_p) you have placed so far. You build the string character by character, following two simple rules:

1)Can I add a (? Yes, as long as open_p < n.

2)Can I add a )? Yes, but only if close_p < open_p. (If you have two ( and two ), adding a third ) creates (())) which can never be recovered).
'''

def parenthesis(n:int) -> list:
    def backtracking(current_str:str, open_p:int, close_p:int):
        if(len(current_str) == 2*n):
            result.append(current_str)
            return
        
        if(open_p < n):
            backtracking(current_str+'(', open_p + 1, close_p)
        if(close_p < open_p):
            backtracking(current_str + ')', open_p, close_p + 1)
            
    result = []
    backtracking('', 0, 0)
    return result
    
            
    
    
    
    
