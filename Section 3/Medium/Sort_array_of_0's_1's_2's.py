# Brute Force Solution

'''
Use any sorting algo
'''

# Better Solution

def sortColors(self, nums: list[int]) -> None:
        count_0 = 0
        count_1 = 0
        count_2 = 0
        for i in range(len(nums)):
            if(nums[i] == 0):
                count_0 += 1
            elif(nums[i] == 1):
                count_1 += 1
            elif(nums[i] == 2):
                count_2 += 1
        for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_1+count_0):
            nums[i] = 1
        for i in range(count_1+count_0, count_2+count_1+count_0):
            nums[i] = 2
            
'''
for i in range(count_0):
            nums[i] = 0
        for i in range(count_0, count_1+count_0):
            nums[i] = 1
        for i in range(count_1+count_0, count_2+count_1+count_0):
            nums[i] = 2
this portion takes O(N) time 

TC - O(2N) - O(N)
SC - O(1)
'''

# Optimized Solution
# Using Dutch National Flag Algo

def sortColors(self, nums: list[int]) -> None:
    # Going to solve the problem using Dutch National Flag Algo

    low, mid = 0, 0
    high = len(nums) - 1
    while(mid<=high):
        if(nums[mid] == 0):
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif(nums[mid] == 1):
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1

'''
TC - O(N)
SC - O(1)
'''
