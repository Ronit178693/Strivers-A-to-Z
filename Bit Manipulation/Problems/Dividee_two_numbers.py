# Brute force solution which can cause an infinite loop for an edge case 
def division(divident, divisor):
    signed_num = False
    if(divident < 0 and divisor < 0 ):
            divident = abs(divident)
            divisor = abs(divisor)
        # Else store the sign of the number
    else:
            
            if(divident < 0):
                signed_num = True
                divident = abs(divident)
            if(divisor < 0):
                signed_num = True
                divisor = abs(divisor)
    count = 0
    while(divident >= divisor):
            count += 1
            divident -= divisor
    if(signed_num):
            count = -count
    if(count > ((2**31) - 1)):
            return (2**31) - 1
    elif(count < -2**31):
            return -2**31
    else:
            return count
        
# Optimal Solution as the dividend is subtracted with its nearest multiple of divisor    
def divide(self, divident: int, divisor: int) -> int:
        signed_neg = False
        if(divident < 0 and divisor < 0):
            divident, divisor = abs(divident), abs(divisor)
        if(divident > 0 and divisor < 0):
            divisor = abs(divisor)
            signed_neg = True
        if(divident < 0 and divisor > 0):
            divident = abs(divident)
            signed_neg = True
        ans = 0
        while(divident >= divisor):
            count = 0
            while(divident >= (divisor << count)):
                count += 1
            ans += 1 << (count - 1)
            divident -= divisor << (count - 1) 
        if(signed_neg == True):
            ans = - ans
        if(ans > ((2**31) - 1)):
            return (2**31) - 1
        elif(ans < -2**31):
            return -2**31
        else:
            return ans
        
        
        