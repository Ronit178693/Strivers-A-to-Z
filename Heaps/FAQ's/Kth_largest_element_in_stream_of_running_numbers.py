class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = []
        for num in nums:
            self.add(num)

    def heapify_down(self, i):
        n = len(self.heap)
        while True:
            smallest = i
            left = (2 * i) + 1
            right = (2 * i) + 2
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if(smallest == i):
                break
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    # Function to store the min heap property of the heap 
    def heapify(self, i):
        parent = abs((i - 1)//2)
        while(True):
            parent = abs((i - 1)//2)
            if(i > 0 and self.heap[i] < self.heap[parent]):
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def add(self, val: int) -> int:
        # If there are no enough elements in the heap then simply add them 
        if(len(self.heap) < self.k):
            self.heap.append(val)
            # When a new element is added we have to store the min heap property of our heap
            self.heapify(len(self.heap) - 1)
        # If val < self.heap[0] then do nothing just pass
        elif(val > self.heap[0]):
            self.heap[0] = val
            self.heapify_down(0)
        return self.heap[0]





# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)