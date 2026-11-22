# Optimal Solution 
class Solution:
    def Maximum(self, nums: list, mid: int):
        maximum_row = -1
        maximum_num = float('-inf')
        for rows in range(len(nums)):
            if(nums[rows][mid] > maximum_num):
                maximum_num = nums[rows][mid]
                maximum_row = rows
        return maximum_row
    def findPeakGrid(self, nums: list[list[int]]) -> list[int]:
        m_rows, n_columns = len(nums), len(nums[0])
        low, high = 0, n_columns - 1
        while(low <= high):
            mid = (low+high)//2
            maximum_row = self.Maximum(nums, mid)
            left = nums[maximum_row][mid - 1] if(mid - 1 >= 0) else float('-inf')
            right = nums[maximum_row][mid + 1] if( mid + 1 <n_columns) else float('-inf')
            if(left < nums[maximum_row][mid] > right):
                return [maximum_row, mid]
            elif(mid - 1 >= 0 and nums[maximum_row][mid] < nums[maximum_row][mid - 1]):
                high  = mid - 1
            else:
                low = mid + 1
        