# Brute Force 
def greater(nums):
    ans = []
    for i in range(len(nums)):
        count = 0
        for j in range(i, len(nums)):
            if(nums[j] > nums[i]):
                count += 1
        ans.append(count)
    return ans 

