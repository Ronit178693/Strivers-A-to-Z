#  Brute Force 
def Finding(num:int, N:int):

    for i in range(1, num + 1):
        if(i**N == num):
            return i
    return -1

'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution

def Finding(num:int, N:int):
    low, high = 1, num
    ans = -1
    while(low<=high):
        mid = (low+high)//2
        if(mid**N == num):
            ans = mid
            break
        elif(mid**N < num):
            low = mid + 1   
        else:
            high = mid - 1
    return ans
