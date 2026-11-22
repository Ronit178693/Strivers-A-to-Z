#  Brute Force 

def zeros(arr:list = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]):
    n = len(arr)
    temp = []
    if( 0 in arr):  
        temp = []  
        for i in arr:
            if(i != 0):
                temp.append(i)
        d = len(temp)
        for i in range(d):
            arr[i] = temp[i]
        for i in range(d, n):
            arr[i] = 0
        return arr
    else:
        return arr

print(zeros())

'''
Best case space: O(1) when no zero is present
Worst case space: O(n) when zero is present and most elements are copied into temp
Time in both cases: O(n)
'''

# Optimal Solution

def move_zeros(arr: list = [1, 0, 2, 3, 2, 0, 0, 4, 5, 1]):
    n = len(arr)
    i = 0

    for j in range(n):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    return arr

print(move_zeros())


'''
TC = O(N)
SC = O(1)
'''

# Leetcode 283 
def moveZeroes(self, nums: list[int]) -> None:
        n = len(nums)
        i = 0
        for j in range(n):
            if(nums[j] != 0):
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums

            
        
            
        
