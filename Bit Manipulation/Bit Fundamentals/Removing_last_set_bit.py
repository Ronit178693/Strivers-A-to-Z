'''
For any number finding the binary value of n - 1 converts the rightmost set to 0 and all the following 0s turn to 1
'''
def removing(num): 
    return num and num-1

'''
40 = 101000
39 = 100111

40&39 = 100000

the right most bit of 40 has been cleared
'''

    
