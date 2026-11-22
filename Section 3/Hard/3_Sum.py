# Brute Force
def sum(nums:list):
    n = len(nums)
    seen = set()
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(nums[i] + nums[j] + nums[k] == 0):
                    ans = []
                    ans.append(nums[i])
                    ans.append(nums[j])
                    ans.append(nums[k])
                    ans.sort()
                    ans_tup = tuple(ans)
                    seen.add(ans_tup)
                    

# Better Solution
def Sum(nums:list):
    ans = set()
    n = len(nums)
    for i in range(n):
        hash = set()
        for j in range(i+1, n):
            req = -(nums[i]+nums[j])
            if(req in hash):
                tuple_ans = tuple(sorted([nums[i], nums[j], req]))
                ans.add(tuple_ans)
            hash.add(nums[j])
    answer = list(ans)
    return answer

# Optimal Solution 

def Sum(nums:list):
    n = len(nums)
    ans = []
    for i in range(n):
        
        
        left, right = i+1, n-1
        
        while(left < right):
            total = nums[i] + nums[left] + nums[right]
            if(total == 0):
                ans.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                while(left < right and nums[left] == nums[left-1]):
                    left += 1
                while(left < right and nums[right] == nums[right - 1]):
                    right -= 1
            elif(total < 0):
                left += 1
            else:
                right -= 1
    return ans 
