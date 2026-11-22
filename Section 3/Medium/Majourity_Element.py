#  Brute force
def Majourity(arr:list):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if(arr[i] == arr[j]):
                count += 1
        if(count > len(arr)//2):
            return i
'''
TC - O(N^2)
SC - O(1)
'''

# Better Solution
# Using Hashing

def Majourity(arr:list):
#  The given array can also has negative elements so we cant represent it in a frequency array
    freq = {}
    for i in range(len(arr)):
        if(arr[i] in freq):
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1
    for j in freq:
        if(freq[j]>len(arr)//2):
            return j
        
'''
TC - O(2N)
SC - O(N)
'''

# Optimized Solution
# Moores Voting Algo

def Majourity(nums:list):
    el = None
    count = 0
    for i in range(len(nums)):
        if(count == 0):
            el = nums[i]
            count = 1
        else:
            if(el == nums[i]):
                count += 1
            else:
                count -= 1
    # This part is for check if the el is in majourity or not 
    cnt = 0
    for j in range(len(nums)):
        if(nums[j] == el):
            cnt += 1
    if(cnt > len(nums)//2):
        return el
        
        
'''
TC - O(2N)
SC - O(1)
'''

            
        
