arr = [3, 2, 1, 5, 2]

# Brute Force solution
def largest_element(arr:list):
    arr.sort()
    return arr[len(arr)-1]

print(largest_element(arr))

'''
The time complexity of Python's .sort() function is \(O(n \log n)\) in the average and worst cases, and O(n) in the best case (when the data is already sorted)

Internally, Python uses Timsort, a hybrid, adaptive, stable sorting algorithm derived from Merge Sort and Insertion Sort. Modern implementations use an optimized version of Timsort called Powersort.
'''

# Better Solution

def largest(arr:list):
    max = arr[0]
    for i in range(1, len(arr)):
        if(arr[i]>max):
            max = arr[i]
    return max

print(largest(arr))

'''
TC = O(N) i.e. better then O(NlogN) of the brute force solution
'''
