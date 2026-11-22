'''
Divide and Conquer Algorithm
Slightly better then Merge sort as it does not uses any aux. space and has a space complexity of O(1) other then the stack space

1) Pick a pivot
2) Place the pivot at its correct position in the sorted array
3) Place all the smaller elements on the left and all the larger elements on the right
4) Repeat these steps to the remaining sides
'''

array = [int(x) for x in input("Enter the elements").split(", ")]

def quickSort(array, low, high):
    if(low == high):
        return
    partitionIndex = partition(array, low, high)
    quickSort(array, low, partitionIndex-1)
    quickSort(array, partitionIndex+1, high)
    return array


def partition(array, low = 0, high = len(array) - 1):
    pivot = array[low]
    i = low
    j = high
    while(i<j):
        # we use >= because we want all the elements smaller then the pivot to be on the left and all the elements greater then the pivot to be on the right
        while(pivot>=array[i] and i<high-1): 
            i += 1
        while(pivot<array[j] and j>low+1):
            j -= 1
        if(array[i]<pivot<array[j] and i<j):
            array[i], array[j] = array[j], array[i]
    array[low], array[j] = array[j], array[low] # We swap with j because j is at an element lower then the pivot if we swap with i it is on the element greater then the pivot and swapping will not place the pivot at its correct position
    return j


'''
O(nlog base 2 n) - Time Complexity 
O(1) - Space Complexity
'''
quickSort(array, 0, len(array)-1)

print(array)