def postfix_to_prefix(s):
    i, stack = 0, []
    while(i < len(s)):
        # If the character encountered is an operand
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            stack.append(s[i])
        # If the charater encountered is an operator
        else:
            character2 = stack.pop()
            character1 = stack.pop()
            string = s[i] + character1 + character2
            stack.append(string )
        i += 1
    return stack.pop()
            
            