# Heapify Up 
def heapify_up(arr, i):
    """
    Moves the element at index i up until the Max-Heap property is restored.
    """
    while i > 0:
        parent = (i - 1) // 2
        
        # In a Max-Heap, if the child is larger than its parent, swap them
        if arr[i] > arr[parent]:
            arr[i], arr[parent] = arr[parent], arr[i]
            i = parent  # Move up to the parent's index
        else:
            break       # Heap property satisfied; stop early

# Heapify down 
def heapify_down(arr, n, i):
    """
    Moves the element at index i down until the Max-Heap property is restored.
    """
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        # Check if left child is larger than current largest
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check if right child is larger than current largest
        if right < n and arr[right] > arr[largest]:
            largest = right

        # If the largest is still the parent, the subtree is stable
        if largest == i:
            break

        # Otherwise, swap and track the element to its new lower level
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
