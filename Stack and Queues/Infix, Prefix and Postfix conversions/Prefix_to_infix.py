def prefix_to_infix(s):
    i, stack = len(s) - 1, []
    while(i >= 0):
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            stack.append(s[i])
        # Postfix expressions does not have any brackets 
        # So we wont write any condition for them 
        # If s[i] is an operator 
        else:
            # Removing and storing the last two elements from the stack to make a string out of them 
            element1 = stack.pop()
            element2 = stack.pop()
            string = '(' + element1 + s[i] + element2 + ')'
            stack.append(string)
        i -= 1
    return stack.pop()
            
            
            