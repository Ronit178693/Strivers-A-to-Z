def heapify(nums, n, i):
    # largest as it should be
    largest = i
    left = (2*i) + 1
    right = (2*i) + 2
    
    # Check if there exists right or left and is greater then the node
    if(left < n and nums[left] > nums[largest]):
        largest = left
    if(right < n and nums[right] > nums[largest]):
            largest = right
            
    # If nothing changes then the tree is all right but if something got changed 
    if(largest != i):
        # Swapping the child and the parent 
        nums[i], nums[largest] = nums[largest], nums[i]
        # Calling back the function to goo down the tree checking the subnodes
        heapify(nums, n, largest)
    
    
def max_heap(nums):
    n = len(nums)
    # Find the last parent node
    last_parent = ((n//2) - 1)
    for i in range(last_parent, -1, -1):
        heapify(nums, n, i)
    