# Brute Force Solution

# Prepare a list of missing integers 

def missing(nums:list, k:int):
        Max = max(nums)
        ans = []
        seen = set(nums)
        for i in range(1,Max+k+1):
            if(i not in seen):
                ans.append(i)
        return ans[k - 1]


# Optimal Solution

def missing(nums:list, k:int):
    low, high = 0, len(nums) - 1
    while(low<=high):
        mid = (low+high)//2
        # Gives number of missing elements on a perticular index
        missing_elements = nums[mid] - (mid+1)
        if(missing_elements<k):
            low = mid + 1
        else:
            high = mid - 1
    # When high crosses low 
    return k+high+1