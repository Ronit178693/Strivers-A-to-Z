def window(nums, k):
    ans = []
    i, j = 0, k - 1
    while(j < len(nums)):
        maxi = float('-inf')
        for k in range(i, j + 1):
            maxi = max(maxi, nums[k])
        ans.append(maxi)
        i += 1
        j += 1
    return ans 

def window(nums, k):
    ans = []
    i = 0
    max_window = nums[i]
    for j in range(1, len(nums)):
        max_window = max(max_window, nums[j])
        if((j - i + 1) == k):
            ans.append(max_window)
            i += 1
    return ans
        
            
            