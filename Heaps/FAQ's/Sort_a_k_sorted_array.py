# Approch 1 - Solve the problem using any sorting algo prefferebly heap sort and return the sorted array this solution takes TC - O(nlogn) and SC - O(1)

class Solution:
    def __init__(self, nums, k):
        self.k = k
        self.heap = []
        result = []
        for num in nums:
            if len(self.heap) < self.k + 1:
                self.heap.append(num)
                self.min_heapify(len(self.heap) - 1)
            else:
                # Heap is full! The root is definitely the next sorted element.
                result.append(self.heap[0])
                
                # Replace the root with the new incoming element and sink it down
                self.heap[0] = num
                self.min_heapify_down(0)
        while len(self.heap) > 0:
            result.append(self.heap[0])
            
            # Move the last element to the root and shrink the heap
            if len(self.heap) > 1:
                self.heap[0] = self.heap.pop()
                self.min_heapify_down(0)
            else:
                self.heap.pop() # Last element removed
                
        return result
    
    def min_heapify_down(self, i):
        n = len(self.heap)
        while(True):
            smallest = i
            left = (2*i) + 1
            right = (2*i) + 2
            if(left < n and self.heap[left] < self.heap[smallest]):
                smallest = left
            if(right < n and self.heap[right] < self.heap[smallest]):
                smallest = right
            if(smallest == i):
                break
            self.heap[smallest], self.heap[i] = self.heap[i], self.heap[smallest]
            i = smallest
        
    def min_heapify(self, i):
        while(True):
            # This is the index of the parent node of the current node
            parent = abs((i-1)//2)
            if(i > 0 and self.heap[i] < self.heap[parent]):
                self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
                i = parent
            else:
                break
            

