'''
1) Swap happens between 0 and min. [0, n-1]
2) Swap happens between 1 and min. [1, n-1]
3) Swap happens between 2 and min. [2, n-1]
4) Swap happens between 3 and min. [3, n-1]


n) Swap happens between n-2 and min. [n-2, n-1]

The outer loop runs from 0 to n-2 for swapping elements and the inner loop runs till n-1 for finding the smallest element
'''

array = [int(x) for x in input("Enter the elements").split(", ")]

for i in range(len(array)-1):
    min = i
    for j in range(i, len(array)):
        if(array[j]<array[min]):
            min = j
    array[i], array[min] = array[min], array[i]
    
print(array)
    
'''
O(n^2) - Time Complexity in all cases 
'''
