# Brute Force Solution Usinf TC - O((end) - start)
def XOR_in_range(start, end):
    for i in range(start, end + 1):
        XOR = XOR ^ i
    return XOR 


# Using the XOR pattern
def Xor(self, num):
    if(num % 4 == 1):
        return 1
    elif(num % 4 == 2):
        return num + 1
    elif(num % 4 == 3):
        return 0
    else:
        return num
    
def xor_in_range(self, start, end):
    xor_start = self.Xor(start - 1)
    xor_end = self.Xor(end)
    
    return xor_start ^ xor_end
    
        