# Optimal Solution
def second_largest(arr:list):
    largest, second_largest = 0, None # Initializing the second largest from -1 1because if we do 0 it starts with the first element and we will not get the second largest
    if(len(arr)>1):
        for i in range(1, len(arr)):
            if(arr[i]>arr[largest]):
                second_largest = largest
                largest = i
            if(arr[i]<arr[largest] and arr[i]>arr[second_largest]):
                second_largest = i
        return arr[second_largest]
    else:
        return "Array should have atleast 2 elements"

# TC = O(N)

# Brute Force Solution

def Second_largest(arr:list):
    largest = 0
    for i in range(1, len(arr)):
        if(arr[i]>arr[largest]):
            largest = i
    
    for j in range(len(arr)):
        if(arr[j]<arr[largest] and (second_largest is None or arr[j]>arr[second_largest])):
            second_largest = j
    return arr[second_largest] if second_largest is not None else "Array should have atleast 2 elements"

# TC = O(N) + O(N) = O(2N) = O(N)