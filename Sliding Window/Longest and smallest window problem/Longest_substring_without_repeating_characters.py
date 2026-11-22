# Brute Force Solution By forming all the possibele substring 
# Using TC - O(N^2) and SC - O(256)
def substring(s):
    n = len(s)
    if(n == 0):
        return 0
    max_length = float('-inf')
    for i in range(n):
        hash = [0] * 256
        for j in range(i, n):
            # We have already found the duplicant and there is no need to find more substrings
            if(hash[ord(s[j])] == 1):
                break
            # we havnt found the duplicate yet and the element was not in the hash array
            else:
                max_length = max(max_length, j - i + 1)
                hash[ord([s[j]])] += 1
    return max_length

# Optimal Solution using sliding window approach 
# Thi solution uses TC - O(N) and SC - O(N)
def substring(s):
        n = len(s)
        hash = {}
        l, r, max_length = 0, 0, 0
        while(r < n):
            # If the element is already in the hash:-
            # 1) Update the left pointer 
            # 2) Update the hash to store the new index of the duplicant 
            # 3) If the duplicant is out of the range then skip it 
            if( s[r] in hash):
                # If the index of duplicant is greater then of the left then the duplicant is in the range. Move l and update its hash
                if(hash[s[r]] >= l):
                    l = hash[s[r]] + 1
                    max_length = max(max_length, r - l + 1)
                    hash[s[r]] = r
                    r += 1
            else:
                max_length = max(max_length, r - l + 1)
                hash[s[r]] = r
                r += 1
        return max_length
            
            
                
                
            
            
                
    
        