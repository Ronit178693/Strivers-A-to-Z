#  Brute Force

def twoSum(self, nums: list[int], target: int) -> list[int]:
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if(i==j):
                continue
            if(nums[i] + nums[j] == target):
                return i, j
            
'''
TC - O(N^2)
SC-O(1)
'''

# Better Solution

def twoSum( nums: list[int], target: int) -> list[int]:
    dir = {} #  Storing the indexes as value and numbers as keys
    for i in range(len(nums)):
        req = target-nums[i] # given k and element x then the second element will be k-x and if that k-x is in the directory we directly return both 
        if(req in dir):
            return [dir[req], i]
        else:
            dir[nums[i]] = i 

'''
TC - O(N)
SC - O(N)
'''

# Optimized Solution

def sum(arr:list, k:int):
    arr.sort()
    i = 0
    j = len(arr)-1
    while(i<j):
        sum = arr[i] + arr[j]
        if(sum<k):
            i += 1
        if(sum>k):
            j += 1
        if(sum == k):
            return i, j        
