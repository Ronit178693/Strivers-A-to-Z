def canJump(self, nums: list[int]) -> bool:
        max_index_reachable = 0
        for i in range(len(nums)):
            if(i > max_index_reachable):
                return False
            max_index_reachable = max(max_index_reachable, (nums[i] + i))
           
        return True