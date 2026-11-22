#  Brute Force Solution

def Union(arr1:list = [1, 1, 2, 3, 4], arr2:list = [2, 3, 4, 4, 5, 6]):
    temp = []
    temp.extend(arr1)
    temp.extend(arr2)
    unique_set = set(temp)
    unique_list = list(unique_set)
    unique_list.sort()
    return unique_list

print(Union())

'''
TC - O(n) + O(m) [Both in filling up temp] + O(n+m) (Forming up a set) + O(K) ( for forming the list) + O(K LOG K) (for sorting) = O(n+m+Klog K)
SC = O(n+m)
'''


# Optimized Solution

def Union(arr1:list = [1, 1, 2, 3, 4], arr2:list = [2, 3, 4, 4, 5, 6]):
    n = len(arr1)
    m = len(arr2)
    Union = []
    seen = set()
    i, j = 0
    while(i<n and j<m):
        if(arr1[i]  in seen and arr2[j]  in seen):
                    i += 1
                    j += 1
                    
        if(arr1[i]<=arr2[j]):
            if(arr1[i] not in seen):
                seen.add(arr1[i])
                Union.append(arr1[i])
                i += 1
            else:
                if(arr2[j] not in seen):
                    seen.add(arr2[j])
                    Union.append(arr2[j])
                    j += 1
        else:
            if(arr2[j] not in seen):
                seen.add(arr2[j])
                Union.append(arr2[j])
                j += 1
            else:
                if(arr1[i] not in seen):
                    seen.add(arr1[i])
                    Union.append(arr1[i])
                    i += 1
    while(j<m):
        if(arr2[j] not in seen):
            seen.add(arr2[j])
            Union.append(arr2[j])
            j += 1
        else:
            j += 1
    while(i<n):
            if(arr1[i] not in seen):
                seen.add(arr1[i])
                Union.append(arr1[i])
                i += 1
            else:
                i += 1
        
            
'''
TC - O(n+m)
SC - O(2(n+m)) = O(n+m)

The SC is slighly better then the brute force solution 
'''
