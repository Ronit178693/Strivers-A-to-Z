def prefix_to_postfic(s):
    i, stack = len(s) - 1, []
    while(i >= 0):
        if((s[i] >= 'A' and s[i] <= 'Z') or (s[i] >= 'a' and s[i] <= 'z') or (s[i] >= '0' and s[i] <= '9')):
            stack.append(s[i])
        else:
            char1 = stack.pop()
            char2 = stack.pop()
            string = char1 + char2 + s[i]
            stack.append(string)
        i -= 1
    return stack.pop()