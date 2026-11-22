'''
A valid parentheses string is a string where every opening bracket has a matching closing bracket, and the brackets are properly nested.

A primitive valid parentheses string is a nonempty valid parentheses string that cannot be split into two smaller nonempty valid parentheses strings.

1) Find the primitive decomposition of the valid parenthesis string 

Intutuin - The number of openning parenthesis = number of closing parenthesis 
'''

# Brute Force
class Solution:
    
    def __init__(self, s:str):
        self.s = s
    
    def primitive_decomposition(self, decomposed:list, s:str) -> list:
        depth = 0
        n, i= len(s), 0
        length = 0
        while(i < n):
            if(s[i] == '('):
                depth += 1
                i += 1
            elif(s[i] == ')'):
                depth -= 1
                i += 1
            if(depth == 0 and length == 0):
                if(len(decomposed) == 0):
                    decomposed.append(s[0:i])
                    length += len[decomposed[0]]
            elif(depth == 0 and length != 0):
                decomposed.append(s[length:i])
                length += len(decomposed[-1])
        return decomposed
    
    def outer_parenthesis_removal(self, s:str) -> list: 
            # Outermost parenthesis = nothing before them and nothing after them
            decomposed = []
            self.primitive_decomposition(decomposed, s)
            for i in range(len(decomposed)):
                decomposed[i] = decomposed[i][1:len(decomposed[i]) - 1]
            return ''.join(decomposed)
        
# Optimal solution without taking extra space 

class Solution:
    
    def __init__(self, s:str):
        self.s = s
    def remove_outermost_parenthesis(s:str) -> str:
        ans = []
        depth = 0
        n, i, length = len(s), 0, 0
        while(i < n):
            if(s[i] == '('):
                depth += 1
                i += 1
            elif(s[i] == ')'):
                depth -= 1
                i += 1
            if(depth == 0):
                string = s[length:i]
                length += len(string)
                string = string[1, len(string) - 1]
                
                
            
            
                
