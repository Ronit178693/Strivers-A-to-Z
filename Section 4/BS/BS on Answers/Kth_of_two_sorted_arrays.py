# Brute force
def merge(num1:list, num2:list):
    i, j = 0, 0
    merged = []
    while(i < len(num1) and j < len(num2)):
        if(num1[i] <= num2[j]):
            merged.append(num1[i])
            i += 1
        else:
            merged.append(num2[j])
            j += 1
    while(i < len(num1)):
        merged.append(num1[i])
    while(j < len(num2)):
        merged.append(num2[j])
    return merged
def median(num1:list, num2:list):
    merged_array = merge(num1, num2)
    n = len(merged_array)
    if(n % 2 == 0):
        return (merged_array[n//2] + merged_array[n//2 - 1]) / 2
    else:
        return merged_array[n//2]