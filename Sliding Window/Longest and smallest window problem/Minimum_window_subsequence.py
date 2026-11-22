# Brute Force Solution 
def window(s1, s2):
    n, m = len(s1), len(s2)
    ans = ''
    min_lenght = 0
    # Hashing s2 
    hash = [0] * m
    for i in range(m):
        hash[ord[s2[i]] - ord('a')] += 1
    # Generating all the subsequences and comparing it with the hash 
    for i in range(n):
        subsequence = ''
        for j in range(i, n):
            subsequence += s1[j]
            if()
            
            