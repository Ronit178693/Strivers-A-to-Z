# Brute Force olution generating all the substrings
def characters(s, k):
    length_substring = 0
    for i in range(len(s)):
        hash = set()
        for j in range(i, len(s)):
            if(s[j] not in hash):
                hash.add(s[j])
            if(len(hash) > k):
                break
            length_substring = max(length_substring, j - i + 1)
    return length_substring

# Optimal solution 
def characters(s, k):
    r, l, length_substring = 0, 0, 0
    hash = {}
    while(r < len(s)):
        if(s[r] not in hash):
            hash[s[r]] = 1
        else:
            hash[s[r]] += 1

        while(len(hash) > k):
            hash[s[l]] -= 1
            if(hash[s[l]] == 0):
                hash.pop(s[l])
            l += 1
        length_substring = max(length_substring, r - l + 1)
        r += 1
    return length_substring
        