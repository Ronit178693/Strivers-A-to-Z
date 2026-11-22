def is_min_heap(arr):
    """
    Returns True if the array represents a valid Min-Heap, 
    and False otherwise.
    """
    n = len(arr)
    
    # Loop through all non-leaf nodes
    for i in range((n // 2)):
        left = 2 * i + 1
        right = 2 * i + 2
        
        # If left child exists and parent is greater than left child
        if left < n and arr[i] > arr[left]:
            return False
            
        # If right child exists and parent is greater than right child
        if right < n and arr[i] > arr[right]:
            return False
            
    return True