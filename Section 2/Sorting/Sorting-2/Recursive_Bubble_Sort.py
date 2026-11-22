array = [int(x) for x in input("Enter the elements").split(", ")]

def bubble_sort(array, n):
    if(n == 1):
        return
    is_swapped = False
    # Running the loop till n-1 because it need to run till n-2 to get compared to the last element 
    for j in range(n-1):
        if(array[j] > array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            is_swapped = True 
    if not is_swapped:
        return
    bubble_sort(array, n-1)

bubble_sort(array, len(array))
print("Sorted array is:", array)    