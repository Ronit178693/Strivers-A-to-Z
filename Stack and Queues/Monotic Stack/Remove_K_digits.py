'''
It is possible to have k = n
'''
def digits(s, k):
    n = len(s)
    stack = []
    # Edge case when k == n
    if(k == n):
        return '0'
    for i in range(n):
        # Using ASCII values for the comparisions of the strings
        while(stack and ((ord(stack[-1]) - ord('0')) > (ord(s[i]) - ord('0'))) and k > 0):
            stack.pop()
            k -= 1
        stack.append(s[i])
    # No element was removed from the stack
    # Remove the last elements from the stack as the string is sorted
    while(k > 0):
        stack.pop()
        k -= 1
    if(len(stack) == 0):
        return '0'
    # Taking O(2N) here 
    result = ("".join(stack)).lstrip('0')
    return result if result else "0"
        
                
            
    
    
        