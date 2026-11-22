# Brute Fore solution : Finding all the substrings, keeping 2 pointers on those substring and checking for every substring is its a palindrome

def palindromic_substring(s:str) ->str:
    def is_palindrome(sub:str) -> bool:
        return sub == sub[::-1]
    n = len(s)
    # 0 or 1 element 
    if(n < 2):
        return s
    longest_substring = ''
    for i in range(n):
        for j in range(i, n):
            
            # substring = s[i:j + 1]
            if(len(longest_substring) < len(s[i:j + 1]) and is_palindrome(s[i:j + 1]) is True):
                longest_substring = s[i:j + 1]
    return longest_substring

# Better solution using O(N^2) TC
# Expand around center method
'''
By looking at the charaters as center and expanding outwards , we eliminate the reductant palindromic check entirely 
'''
'''
A palindrome mirrors from its center. We can loop through the string and treat each position as a potential center, expanding left and right as long as the characters match
'''
def expand(left:int, right:int, s:str):
    n = len(s)
    # Moves until the boundary pointers missmatches
    while(left >= 0 and right < n and s[left] == s[right]):
        left -= 1
        right += 1
    # returning the length of the palindrome found
    return right - left - 1

def palandromic_string(s:str):
    start, end = 0, 0
    longest = 0
    
    for i in range(len(s)):
        
        '''
        Each element in the string is considered as center and the length of palindrome is found from each center via expanding. As the palindromes can be both even/ odd lengthed we find length for both and the length will be maximum in either case 
        '''
        # When the palindrome is odd
        len1 = expand(i, i)
        # When the palindrome is even 
        len2 = expand(i, i+1)
        
        longest = max(len1, len2)
        
        if(longest > (end - start)):
            start = i - (longest - 1) // 2
            end = i + longest // 2
    return s[start:end+1]
            
         
        
    

    

    


            
        

                
                

                    
                    
                
            