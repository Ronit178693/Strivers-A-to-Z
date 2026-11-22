# Brute Force
def lower_bound(nums:list, x:int):
    n = len(nums)
    for i in range(n):
        if(nums[i]>x):
            return i
    return len(nums) # There exists no element that satisfies the above condition so we return the insertion position of x
'''
TC - O(N)
SC - O(1)
'''

# Optimal Solution
def lower_bound(nums:list, x:int):
    low, high = 0, len(nums) - 1
    ans = len(nums) # Considering there is no element which passes our condition of lower bound
    while(low<=high):
        mid = (low+high)//2
        # In the case where mid = x we will also have to check for the elements in the left half
        # if(nums[mid] == x):
        #     return mid
        if(nums[mid]>x):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

'''
TC - O(logn)
SC - O(1)
'''

            
    

