
arr = [int(x) for x in input("Enter the elements of the array separated by space: ").split(', ')]

def rotation(arr:list):
    temp = arr[0]
    for i in range(1, len(arr)):
        arr[i-1] = arr[i]
    arr[len(arr)-1] = temp
    return arr

print("Original array:", arr)
print("Array after left rotation by one position:", rotation(arr))

'''
TC - O(N)
SC - O(1) as we are using costant space even if we are using temp variable it only has a single element in it

SC = Input Spce + Auxilary Space 

so SC = O(N) + O(1) = O(N) for this case 
'''




     
        