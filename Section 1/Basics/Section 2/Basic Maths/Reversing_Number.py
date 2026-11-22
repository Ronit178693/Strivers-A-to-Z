n = int(input("Enter a number: "))
rev = 0
while(n!=0):
    digit = n%10
    rev = rev*10 + digit
    n //= 10
print("Reversed number:", rev)


# Leetcode 7
class Solution:
    def reverse(self, x: int) -> int:
        is_neg = x<0  # Storing the sign of the value
        rev_int = 0
        x = abs(x)  # Taking the absolute value of the number to reverse it
        while(x != 0):
            last_num = x%10
            x = x//10
            rev_int = (rev_int*10)+last_num # Reversing the number
        if(is_neg):
            rev_int = -rev_int # If the number is negative, we will make the reversed number negative
        if(-2**31<=rev_int<=((2**31)-1)): # Checking if the reversed number is in the range of 32 bit signed integer
            return rev_int
        else:
            return 0
        
       