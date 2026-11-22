'''
Monotonic stack = Storing elements in the stack in an specific order 
'''

# This solution is the bRute force approch using O(N*M*k) as TC and O(N) as SC 
'''
This solution is also imp because it uses the concept of for ...  else 
'''

def NGE(nums1, nums2):
        ans = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                # When we have found the matchign element in nums 2
                if(nums1[i] == nums2[j]):
                    for k in range(j + 1, len(nums2)):
                        if(nums2[k] > nums2[j]):
                            ans.append(nums2[k])
                            break
                    else:
                        ans.append(-1)
                        break
        return ans 
    
# Better solution using hashmap and storing the mapped indexes 
def NGE(nums1, nums2):
    ans = []
    hash = {}
    # Storing the hashed index map for nums2 for fast lookup of elements while comparing 
    for i in range(len(nums2)):
        hash[nums2[i]] = i
    for i in range(len(nums1)):
        for j in range(hash[nums1[i]] + 1, len(nums2)):
            if(nums2[j] > nums1[i]):
                ans.append(nums2[j])
                break
        else:
            ans.append(-1)
    return ans

'''
TC - O(M*N)
SC - O(2N) - O(N)
'''

# Optimal Solution 
'''
Here instead of looking for the elements in nums1 we just perform calculation for each and every element in nums2 then populate the ans list with respect to the nums1
'''

def NGE(nums1, nums2):
    hash = {}
    stack = []
    ans = []
    
    for i in range(len(nums2) - 1, -1, -1):
        while(stack and nums2[i] >= stack[-1]):
            stack.pop()
        if(not stack):
            hash[nums2[i]] = -1
        else:
            hash[nums2[i]] = stack[-1]
        stack.append(nums2[i])

    for i in nums1:
        ans.append(hash[i])
    return ans
        


                
        
                