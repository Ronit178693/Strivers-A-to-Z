# Brute Force Solution taking TC - O(3^N) and SC - O(N)
def valid_parenthesis(s):
    def generate(s, indx, count):
        # If the string is starting with closing parenthesis then it can never be valid
        if(count < 0):
            return False
        # If till the last index count is not 0 then the string is not valid else it is valid
        if(indx == len(s)):
            return (count == 0)
        
        if(s[indx] == '('):
            return generate(s, indx + 1, count + 1)
        if(s[indx] == ')'):
            return generate(s, indx + 1, count - 1)
        # If it is a * 
        return generate(s, indx + 1, count + 1) or generate(s, indx + 1, count - 1) or generate(s, indx + 1, count)
    return generate(s, 0, 0)

# Optimal Solution 
# Carrying a range of count 
# TC - O(N) and SC - O(1)
def valid_parenthesis(s):
    min, max = 0, 0
    for i in range(len(s)):
        if(s[i] == '('):
            min += 1
            max += 1
        if(s[i] == ')'):
            min -= 1
            max -= 1
        if(s[i] == '*'):
            # In case of * the range can be [-1, 1]
            min -= 1
            max += 1
        if(min < 0):
            min = 0
        if(max < 0):
            return False
    # When the loop is finished and we have got our range of count 
    return (min == 0)
        
    
            
             