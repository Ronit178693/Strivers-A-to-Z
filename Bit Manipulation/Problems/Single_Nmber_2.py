# Brute Force Solution to this problem using hashing 

# Better Solution 
def singleNumber(self, nums: list[int]) -> int:
        sorted_nums = nums.sort()
        # Every nums will have a minimum of 4 elements 
        i = 1
        while(i < len(nums)):
            if(nums[i - 1] == nums[i]):
                # checking if the first element of the list is the element we are searching for if not then its a triplet and we move 3 places ahead 
                i += 3
            elif(nums[i - 1] != nums[i]):
                return nums[i - 1]
        return nums[len(nums) - 1]
    
# Optimal Solution 
def singleNumber(self, nums: list[int]) -> int:
        ones, twos = 0, 0
        for i in range(len(nums)):
            # a value goes to ones if its not in twos
            ones = (ones ^ nums[i]) & ~(twos)
            # a value goes to twoes if its already in ones 
            twos = (twos ^ nums[i]) & ~(ones)
        return ones