# Brute Force Solution 
def substring(s, t):
    if(len(s) < len(t)):
        return ''
    length = float('inf')
    starting_indx = -1
    for i in range(len(s)):
        # Storing the t string in the frequency table
        hash = [0] * 256
        count = 0
        for k in range(len(t)):
            hash[ord(t[k])] += 1
        for j in range(i, len(s)):
            if(hash[ord(s[j])] > 0):
                count += 1
            hash[ord(s[j])] -= 1 
            # We have found the substring with the occurence
            if(count == len(t)):
                if(j - i + 1 < length):
                    length = j - i + 1
                    starting_indx = i
                    break
    return s[starting_indx : length + 1]



# Optimal Solution 
def substrings(s, t):
    if(len(s) < len(t)):
        return ''
    r, l, count = 0, 0, 0
    min_length = float('inf')
    starting_indx = -1
    # Pre-hashing the t string
    hash = [0] * 256
    for i in range(len(t)):
        hash[ord(t[i])] += 1

    while(r < len(s)):
        # If the element was pre inserted in the hash map
        if(hash[ord(s[r])] > 0):
            count += 1
        while (count == len(t)):
            # Calculating the starting index and the minimum length
            if(r - l + 1 < min_length):
                min_length = r - l + 1
                starting_indx = l
            # shrink the window until the condition gets false
            hash[ord(s[l])] += 1
            # This can only happen for the elements in t 
            if(hash[ord(s[l])] > 0):
                count -= 1
            l += 1
        hash[ord(s[r])] -= 1 
        r +=1 
    if(starting_indx == -1):
        return ''
    return s[starting_indx : starting_indx + min_length]
         