# Brute Force solution taking TC - O(nlogn) and SC - O(n)
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
       
        hash = {}
        for i in range(len(nums)):
            # If element not in hash just add one to the hash 
            if(nums[i] not in hash):
                hash[nums[i]] = 1
            # If the element is already in the hash increaze its frequency 
            else:
                hash[nums[i]] += 1

        ans = []
        sorte= sorted(hash.items(), key=lambda item: item[1], reverse = True)
        for i in range(k):
            ans.append(sorte[i][0])
        return ans
    


class Solution:
    # Thsi function hashes the given array
    def hashed(self, nums):
        hash = {}
        for i in range(len(nums)):
            # If element not in hash just add one to the hash 
            if(nums[i] not in hash):
                hash[nums[i]] = 1
            # If the element is already in the hash increaze its frequency 
            else:
                hash[nums[i]] += 1
        return hash


    def heapify_down(self, i, heap):
        n = len(heap)
        while(True):
            smallest = i
            left = (2*i) + 1
            right = (2*i) + 2
            if(left < n and heap[left] < heap[smallest]):
                smallest = left
            if(right < n and heap[right] < heap[smallest]):
                smallest = right
            if(smallest == i):
                break
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest


    def heapify_up(self, i, heap):
        while(True):
            parent = (i-1)//2
            if(i > 0 and heap[parent] > heap[i]):
                heap[parent], heap[i] = heap[i], heap[parent]
                i = parent
            else:
                break


    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        heap = []
        # Have the hash dict
        hashed = self.hashed(nums)
        for num, freq in hashed.items():
            pair = (freq, num)
            if(len(heap) < k):
                heap.append(pair)
                self.heapify_up(len(heap) - 1, heap)
            elif pair[0] > heap[0][0]:
                heap[0] = pair
                self.heapify_down(0, heap)
        ans = []
        for i in heap:
                ans.append(i[1])
        return ans