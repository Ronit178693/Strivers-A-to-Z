n = int(input("Enter a number: "))
original = n
rev_int = 0
while(n != 0):
    digin = n%10
    n //= 10
    rev_int = (rev_int*10)+digin

if(original == rev_int):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    
    
# Leetcode 9 

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x==0):
            return True
        if(x>0):
            original = x
            reverse_num = 0
            while(x != 0):
                last_num = x%10
                x //= 10
                reverse_num = reverse_num*10 + last_num
            if(reverse_num == original):
                return True
            else:
                return False
        else:
            return False
