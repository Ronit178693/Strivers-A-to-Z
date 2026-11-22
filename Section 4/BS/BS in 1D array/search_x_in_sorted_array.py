# Iterative Approache
def bs(nums:list, target:int):
    low, high = 0, len(nums) - 1
    while(low <= high):
        mid = (low+high)//2
        if(nums[mid] == target):
            return mid
        elif(nums[mid]>target):
            high = mid - 1
        else:
            low = mid + 1
    return -1 # When we loop through the array and dont find the target 

'''
TC - O(logn) - The search space gets half after each comparision
SC - O(1)
'''

# Recursive Approache
def bs(self, nums:list[int], target:int, low:int, high:int):
        mid = (low+high)//2
        if(low>high):
            return -1
        if(nums[mid] == target):
            return mid
        elif(nums[mid] > target):
            return self.bs(nums, target, low, mid - 1) # as this receives some value 
        else:
            return self.bs(nums, target, mid+1, high)
def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        return self.bs(nums, target, low, high)
    
