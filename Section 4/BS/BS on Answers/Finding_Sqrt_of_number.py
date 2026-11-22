# Brute Force Solution
def Sqrt(num:int):
    ans = 1
    for i in range(1, num+1):
        if(i*i <= num):
            ans = i
        else:
            break
    
'''
TC - O(N)
SC - O(1)
'''

# Better Soluution
import math
def Sqrt(num:int):
    return math.sqrt(num)

'''
TC - O(1)
SC - O(1)
'''

# Optimal Solution

def sqrt(num:int):
    low, high = 1, num
    while(low<=high):
        mid = (low+high)//2
        if(mid*mid <= num):
            low = mid + 1
        else:
            high = mid - 1
    return high

'''
TC - O(logn)
SC - O(1)
'''
