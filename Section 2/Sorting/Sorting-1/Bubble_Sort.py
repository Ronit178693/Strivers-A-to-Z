'''
Pushes the maximum to the last by adj. swapping

1) Space = [0, n-1]
2) Space = [0, n-2]
3) Space = [0, n-3]



n) Space = [0, 1]
There is no point of comparing the first element with itself


'''
array = [int(x) for x in input("Enter the elements").split(", ")]

for i in range(len(array)-1, 0, -1 ):
    for j in range(0, i):
        if(array[j]>array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]

print(array)

'''
O(n^2) - Time Complexity in Worst and Average case
'''



'''
Optimization if the array is already sorted then we dont have to perform checks at every step we just have to check if any swap happend in the first iteration of the outer loop if yes the array was not originally sorted and needed to be sorted

O(n) - Time Complexity in Best case
'''

for i in range(len(array)-1, 0, -1 ):
    didntSwaps = True
    for j in range(0, i):
        if(array[j]>array[j+1]):
            array[j], array[j+1] = array[j+1], array[j]
            didntSwaps = False
    if(didntSwaps):
        break
    
print(array)