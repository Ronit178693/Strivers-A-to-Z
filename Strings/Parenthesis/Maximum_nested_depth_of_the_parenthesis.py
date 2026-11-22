'''
The nesting depth of a parentheses string is the maximum number of open parentheses that are nested inside each other at any single point in the string.
'''
# Brute Force
def nested_depth(s:str) -> int:
    seen = set()
    depth = 0
    n = len(s)
    i = 0
    while(i < n):
        if(s[i] == '('):
            depth += 1
            seen.add(depth)    
        elif(s[i] == ')'):
            depth -= 1
            seen.add(depth)
        i += 1
    if(len(seen) == 0):
        return 0
    return max(seen)

# Take O(n) of space 

# Optimal Solution 
def maxDepth(s:str) -> int:
    Max = 0
    depth = 0
    n = len(s)
    i = 0
    while(i < n):
        if(s[i] == '('):
            depth += 1
            Max = max(Max, depth)
        elif(s[i] == ')'):
            depth -= 1
        i += 1
    return Max