# Brute Force Solution finding all the substrings in O(N^2) TC 
def number_of_substrings(s:str) -> int:
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            count += 1
    return count

# Optimal Solution using TC O(N)
def number_of_substrings(s:str) -> int:
    count = 0
    for i in range(1, len(s) + 1):
        count += i
    return count
'''
Shift your perspective from "where does a substring start" to "where does a substring end
'''
