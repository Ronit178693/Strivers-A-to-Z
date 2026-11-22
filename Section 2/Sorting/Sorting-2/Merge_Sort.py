''''
Divide and Conquer Algorithm, First divide the array and the merge it 

In the case of an array with odd number of elements them we can divide the array in any order but we prefer len(array)//2 that is the floor division 

The division is just hypothetical we dont really break the array into two parts every time 

'''

array = [int(x) for x in input("Enter the elements").split(", ")]
low, high = 0, len(array) - 1


def merge(array, low, mid, high):
    temp = []
    i, j = low, mid+1
    while(i<=mid and j<=high):
        if(array[i]<=array[j]):
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while(i<=mid):
        temp.append(array[i])
        i += 1
    while(j<=high):
        temp.append(array[j])
        j += 1
        
    for z in range(len(temp)):
        array[z] = temp[z]

def mergeSort(array, low, high):
    if(low>=high):
        return
    mid = len(array)//2
    mergeSort(array, low, mid)
    mergeSort(array, mid+1, high)
    merge(array, low, mid, high)
        
        
'''
O(N log base 2 N) - Time Complexity in all cases

O(N) - Space Complexity in all cases

'''
