string = input("Enter the string: ")

def is_palindrome(string:str, i:int = 0):
    if(i>=len(string)//2):
        return True
    if(string[i] != string[len(string)-i-1]):
        return False
    return is_palindrome(string, i+1)

print(is_palindrome(string))
        
        
# Leetcode 125

class Solution:
    def isPalindrome(self, s: str, start:int = 0) -> bool:
#         # Firstly we conver the phrase to lowecase letters 
#         # As strings are immutable we have to store the lowercased phrase somewhere
#         lowercased = s.lower()
#         # Now we remove all the non-alphanumeric characters
#         cleaned_list = [x for x in lowercased if(x.isalnum())] # Coverts the phrase to alphanumeric numbers leaving the phrase only with numbers and string 
#         cleaned_string = "".join(cleaned_list) # Joins the list and converts it to a string
#         # Now we have a cleaned string in lowercase letters
#         # Now we check if its a palindrome or not
#         if(start>=len(cleaned_string)//2):
#                  return True # Tre hits when we reaches the base condition without any missmatch
#         if(cleaned_string[start] == cleaned_string[len(cleaned_string)-start-1]):
#             return(self.isPalindrome(s, start+1)) # We cannot bliendly return true we will return what the function tells us 
#         else:
#             return False
        
        
# The recursive solution fails due to a verry large input so we will solve this using 2 pointer approache

        cleaned = "".join([char.lower() for char in s if char.isalnum()])

        end = len(cleaned)-1
        while(start < end):
            if(cleaned[start] != cleaned[end]):
                return False
            else:
                start += 1
                end -= 1
        return True
        