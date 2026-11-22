
def linear_search(arr:list, k:int):
    for i in range(len(arr)):
        if(arr[i] == k):
            return i
    return None
'''
TC - O(N)
SC - O(1)
'''
