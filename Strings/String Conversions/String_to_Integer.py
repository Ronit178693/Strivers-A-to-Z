'''
Whitespace: Ignore any leading whitespace (" ").

Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity if neither present.

Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.

Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
'''

'''Edge Cases : ''' 

def myAtoi(self, s: str) -> int:
    s.lstrip(' ')
    if(s[0] == '-'):
        sign = '-'
    else:
        sign = '+'
    n = len(s)
    i = 1
    while(i < len(s) - 1 and s[i].isdigit()):
        if(s[i] == 0):
            i += 1
            continue
        else:
            i += 1
        