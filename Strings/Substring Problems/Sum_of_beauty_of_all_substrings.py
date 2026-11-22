# Brute force solution using TC = O(N^3) and SC = O(N)
def beauty(sub:str):
    frequency_table = [0] * 26
    for i in sub:
        index = ord(i) - ord('a')
        frequency_table[index] += 1
    '''
    case 1 = When the string is aaa there is no element with min. frequency so min frequency is 0 and max is 3 beauty = 3
    (The above case is invalid as both max and min will be 3 in this case making beauty = 0)
    case 2 = When the string is aaaccb, the frequency map is 3 - a, 2 - c, 1 - b, so the beauty is 3-1 = 2, not 3-2
    case 3 = When the string aaab, the frequency map is 3 - a, 1 - b, the beauty is 3-1 = 2
    '''
    
    new_table = [freq for freq in frequency_table if(freq > 0)]
    return max(new_table) - min(new_table)
        
def substrings(s:str):
    total_beauty = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j + 1]
            substring_beauty = beauty(substring)
            total_beauty += substring_beauty
    return total_beauty


# Optimal Solution ( we will completely elminate creating a seperate hash table for every substring)

def beauty(s:str):
    total_beauty = 0
    for i in range(len(s)):
        # Creating a frequency hash for a set of substrings with same starting point
        freq_list = [0] * 26
        for j in range(i, len(s)):
            index = ord(s[j]) - ord('a')
            freq_list[index] += 1
            
            freq_list_without_0 = [freq_list[freq] for freq in range(len(freq_list)) if (freq_list[freq] > 0)]
            
            total_beauty += max(freq_list_without_0) - min(freq_list_without_0)
    return total_beauty
            