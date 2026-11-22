# Brute Force Solution 
def substrings(s):
    n = len(s)
    count = 0
    for i in range(n):
        hash = [0] * 3
        for j in range(i, n):
            hash[s[j] - 'a'] = 1
            if(hash[0] + hash[1] + hash[2] == 3):
                count += 1
    return count 
            
            
# Optimal Solution 
def substrings(s):
    a, b, c = -1, -1, -1
    count = 0
    for i in range(len(s)):
        if(s[i] == 'a'):
            a = i
        elif(s[i] == 'b'):
            b = i
        else:
            c = i
        if(a != -1 and b != -1 and c != -1):
            count += (1 + min(a, b, c))
    return count