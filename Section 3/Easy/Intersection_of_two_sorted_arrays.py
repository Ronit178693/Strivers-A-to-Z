#  Brute Force

def Intersection(arr1:list = [1, 2, 2, 3, 3, 4, 5, 6], arr2:list = [2, 3, 3, 5, 6, 6, 7]):
    visited = [0] * len(arr2) # As we are keeping track of arr2
    Intersection = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if(arr1[i] == arr2[j] and visited[j] == 0):
                Intersection.append(arr1[i])
                visited[j] += 1
                break
    return Intersection

print(Intersection())


'''
TC - O(N^2)
SC - O(2N)
'''

                
    
     