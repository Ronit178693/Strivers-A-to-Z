'''
If the bit conversion of the number only has one set bit that is 2^x only one bit with value 1 then that number will be tru if their are none or more set bits then the number wont be true 
'''

def checkingg(n):
    if(n == 0):
            return False
    if((n&n-1) == 0):
            return True
    return False
         
