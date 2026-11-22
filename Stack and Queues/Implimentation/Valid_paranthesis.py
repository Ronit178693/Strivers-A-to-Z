# Preserve the opening bracket to later match it with its corresponding closing bracket 
# Every closing bracket is matched with the last opening bracket encountered so we will use Stack as it uses LIFO mechanism

def paranthesis(s):
    stack = []
    for i in range(len(s)):
        # If its an opening bracket push to stack
        if(s[i] == '(' or s[i] == '[' or s[i] == '{'):
            stack.append(s[i])
        # Otherwise compare the closing one with the last element pushed in the stack 
        else:
            # There was no opening bracket corresponding to the closing brackets 
            if(len(stack) == 0):
                return False
            # Gives the top of the stack
            ch = stack[len(stack) - 1]
            # If the closing matches the last pushed then the string is valid and the element gets popped out of the stack 
            if((s[i] == ')' and ch == '(') or (s[i] == ']' and ch == '[') or (s[i] == '}' and ch == '{')):
                stack.pop()
            # If the elements does not form a valid string then return false 
            else:
                return False
    # After processing all the elements of the string check if something is left in the stack or not 
    if(len(stack) == 0):
        return True
    else:
        return False
                
            
                
    