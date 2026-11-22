def infix_to_postfix(s):
    priority = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3 
    }
    i, st, ans = 0, [], ''
    while(i < len(s)):
        # If the char is an operand
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            ans += s[i]
        # If its an opening bracket 
        elif(s[i] == '('):
            st.append(s[i])
        # If the element is a closing bracket then keep poping elements out of the stack until the opening bracket is encountered and keep adding the elements to the ans
        elif(s[i] == ')'):
            while(st and st[len(st) - 1] != '('):
                element = st.pop()
                ans += element
            # For poping out the closing brackets too 
            st.pop()  
        else:
            while(st and priority[s[i]] <= priority[st[len(st) - 1]]):
                ans += st[len(st) - 1]
                st.pop()
            st.append(s[i])
        i += 1
    while(st):
        ans += st[len(st) - 1]
        st.pop()
    return ans
                
                
            
            