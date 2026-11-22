# Brute force 

def Majourity(nums:list):
    n = len(nums)
    ls = []
    for i in range(len(nums)):
        if(nums[i] not in ls):
            count = 0 
            for j in range(len(nums)):
                if(nums[i]==nums[j]):
                    count += 1
                if(count > n//3):
                    ls.append(nums[i])
                    break
        
'''
TC - O(N^2)
SC ~ O(1) As ls will have at max 2 elements
'''

                
                
# Better Soution

def Majourity(nums:list):
    freq = {}
    n = len(nums)
    ls = []
    for i in range(len(nums)):
        if(nums[i] not in freq):
            freq[nums[i]] = 1
        else:
            freq[nums[i]] += 1
    for i in freq:
        if(freq[i] > n//3):
            ls.append[i]
          
'''
TC - O(2N)
SC ~ O(N)
'''
  
        
def Majourity(nums:list):
    freq = {}
    n = len(nums)
    ls = []
    for i in range(len(nums)):
        if(nums[i] not in freq):
            freq[nums[i]] = 1
        else: 
            freq[nums[i]] += 1
            
        if(nums[i] not in ls):
            if(freq[nums[i]] > n//3):
                ls.append(nums[i])
                
    return ls

'''
TC ~ O(N)
SC ~ O(N)
'''

# Optimal Approache

def Majourity(nums:list):
    n = len(nums)
    el1 = None
    el2 = None
    counter1 = 0
    counter2 = 0
    for i in range(len(nums)):
        if(counter1 == 0 and nums[i] != el2):
            el1 = nums[i]
            counter1 += 1
        elif(counter2 == 0 and nums[i] != el1):
            el2 = nums[i]
            counter2 += 1
        elif(nums[i] == el1):
            counter1 +=1
        elif(nums[i] == el2):
            counter2 += 1
        else:
            counter1 -= 1
            counter2 -= 1
    count1 = 0
    count2 = 0
    for i in range(len(nums)):
        if(el1 == nums[i]):
                count1 += 1
        if(el2 == nums[i]):
            count2 += 1
    if(count1 > n//3 and count2 > n//3):
        return [el1, el2]
    elif(count1>n//3):
        return [el1]
    elif(count2>n//3):
        return [el2]
    else:
        return []
    
'''
TC - O(2N)
SC - O(1)
'''

            
        