# Solutions when pos == neg 

# Brute Force 
def Rearrange(nums:list):
    possitive = []
    negative = []
    
    for i in range(len(nums)):
        if(nums[i]>0):
            possitive.append(nums[i])
        else:
            negative.append(nums[i])
    '''
    we have seperated all the +ves and -ves now we want the +ve to appear first at 0th index 
    then a -ve number at 1st index and soo on. We can see that all the +ves appear at even index
    and all the -ves at odd index
    '''
    for i in range(len(possitive)):
        nums[2*i] = possitive[i]
        nums[(2*i)+1] = negative[i]
    return nums

'''
TC - O(N + N/2) - O(N)
SC - O(N/2) + O(N/2) = O(N)
'''

# Optimized Solution

def Reaarrange(nums:list):
    n = len(nums)
    ans = [0] * n
    pos = 0
    neg = 1
    for i in range(n):
        if(nums[i] > 0):
            ans[pos] = nums[i]
            pos += 2
        else:
            ans[neg] = nums[i]
            neg += 2
    return ans

'''
TC - O(N)
SC - O(N)
'''


# No such condition as there are equal number of each type of element 


def Rearrange(nums:list):
    pos = []
    neg = []
    for i in range(len(nums)):
        if(nums[i] >= 0):
            pos.append(nums[i])
        else:
            neg.append(nums[i])
    if(len(pos) > len(neg)):
        for i in range(len(neg)):
            nums[2*i] = pos[i]
            nums[(2*i)+1] = neg[i]
        for j in range(2*len(neg), len(pos)):
            nums[j] = pos[j]
    else:
        for i in range(len(pos)):
            nums[2*i] = pos[i]
            nums[(2*i)+1] = neg[i]
        for j in range(2*len(pos), len(neg)):
            nums[j] = neg[j]
    return nums