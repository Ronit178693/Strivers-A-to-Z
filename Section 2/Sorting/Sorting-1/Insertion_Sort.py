'''
Takes an element and places it in its correct position
'''

array = [int(x) for x in input("Enter the elements").split(", ")]

for i in range(len(array)):
    j = i
    while(j>0 and array[j-1]>array[j]):
        array[j-1], array[j] = array[j], array[j-1]
        j -= 1
        
print(array)


'''
O(N^2) - Time Complexity in Worst and Average case
O(N) - Time Complexity in Best case
'''
