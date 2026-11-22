def subsets(self, nums: list[int]) -> list[list[int]]:
        # the list used to return the answer 
        ans = []
        for i in range(1 << len(nums)):
            temp = []
            for j in range(len(nums)):
                if(i & (1 << j) != 0):
                    temp.append(nums[j])
             
            ans.append(temp)
        return ans