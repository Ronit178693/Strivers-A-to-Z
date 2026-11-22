def infix_to_prefix(s):
    priority = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3 
        }
    i, st, ans = 0, [], ''
    s.reverse()
    while(i <len(s)):
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            ans += s[i]
        elif(s[i] == '('):
            st.append(s[i])
        elif(s[i] == ')'):
            while(st and st[len(st) - 1] != '('):
                 element = st.pop()
                 ans += element
            # For poping out the closing brackets too 
            st.pop()
        else:
            # if the priority of element s[i] >= to the priority of the element in stack just keep appending the element to the stack 
            # But is the priority is strictly less then then pop the element from the stack 
            while(st and priority[s[i]] < priority[st[len(st) - 1]]):
                ans += st[len(st) - 1]
                st.pop()
            st.append(s[i])
        i += 1
    while(st):
         ans += st[len(st) - 1]
         st.pop()
    ans.reverse()
    return ans
        