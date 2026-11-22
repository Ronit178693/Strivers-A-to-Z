# Brute Force Solution 
def repeating(s, k):
    max_len = 0
    for i in range(len(s)):
        hash = [0] * 26
        max_freq = 0
        for j in range(i, len(s)):
            hash[ord(s[j]) - ord('A')] += 1
            max_freq = max(max_freq, hash[ord(s[j])])
            changes = (j - i + 1) - max_freq
            if(changes <= k):
                max_len = max(max_len, j - i + 1)
            else:
                break
    return max_len

# Optimal Solution 
def repeating(s, k):
    l, r, max_len, max_freq = 0, 0, 0, 0
    hash = [0] * 26
    while(r < len(s)):
        hash[ord(s[r]) - ord('A')] += 1
        max_freq = max(max_freq, hash[ord(s[r]) - ord('A')])
        
        # If the changing elements are more then k 
        while((r - l + 1) - max_freq > k):
             hash[ord(s[l]) - ord('A')] -= 1
             max_freq = max(hash) 
             l +=1 
             
        if((r - l + 1) - max_freq <= k):
            max_len = max(max_len, r - l + 1)
        r += 1
    return max_len            
                        