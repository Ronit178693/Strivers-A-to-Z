def ceil(nums:list, x:int):
    low, high = 0, len(nums) - 1
    ans = -1
    while(low<=high):
        mid = (low+high)//2
        # In the case where mid = x we will also have to check for the elements in the left half
        # if(nums[mid] == x):
        #     return mid
        if(nums[mid]>=x):
            ans = nums[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans
def floor(nums:list, x:int):
    low, high = 0, len(nums) - 1
    ans = -1 # Return -1 if floor or ceil does not exists
    while(low<=high):
        mid = (low+high)//2
        if(nums[mid] <= x):
            ans = nums[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans

def floor_ceil(nums:list, x:int):
    return [ceil(nums, x), floor(nums, x)]

'''
TC - O(log n)
SC - O(1)
'''
