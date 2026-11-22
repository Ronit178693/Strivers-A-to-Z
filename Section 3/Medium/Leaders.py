# Brute Force

def Leader(nums:list):
    n = len(nums)
    ans = []
    for i in range(n):
        is_Leader = True
        for j in range(i + 1, n):
            if(nums[i] < nums[j]):
                is_Leader = False
                break
        if(is_Leader == True):
            ans.append(nums[i])
            
'''
TC - O(N^2)
SC - O(N)
'''

# Optimal Solution
def Leaders(nums:list) -> list:
    ans = []
    n = len(nums)
    max = -float('inf')
    for i in range(n-1, -1, -1):
        if(nums[i] > max):
            max = nums[i]
            ans.append(nums[i])
    return ans

'''
TC - O(N)
SC - O(N)
'''

    

            