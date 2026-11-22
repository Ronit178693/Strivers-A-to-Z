class Solution:
    def heapify(self, nums, n, i):
        largest = i
        left = (2*i) + 1
        right = (2*i) + 2

        if(left < n and nums[left] > nums[largest]):
            largest = left
        if(right < n and nums[right] > nums[largest]):
            largest = right
        if(largest != i):
            nums[largest], nums[i] = nums[i], nums[largest]
            self.heapify(nums, n, largest)
    def findKthLargest(self, nums: list[int], k: int) -> int:
        n = len(nums)
        last_parent = (n//2) - 1
        for i in range(last_parent, -1, -1):
            self.heapify(nums, n, i)
        for i in range(n - 1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return nums[-k]
        