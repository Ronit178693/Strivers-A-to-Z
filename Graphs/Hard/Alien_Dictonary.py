from collections import deque
def alien(words):
    # Find out all the unique chars in the dictonay, which later helps building the graph and mapping elements back to the resultant array 
    
    char_to_indx = {}
    indx_to_char = []
    
    for word in words:
        for char in word:
            if(char not in char_to_indx):
                char_to_indx[char] = len(indx_to_char)
                indx_to_char.append(char)
    total_chars = len(indx_to_char)
    
    # Now we have all the chars, we now have to build the directed graph by finding the distinctions in adj. words 
    
    adj_list = []
    in_degree = []
    for _ in range(total_chars):
        adj_list.append(set())
        in_degree.append(0)
    
    for i in range(len(words) - 1):
        word_1 = words[i]
        word_2 = word[i + 1]
        # Edge case = if len(word1) > len(word2) and word1 starts with word 2 then we cant distinguish them 
        if(len(word_1) > len(word_2) and word_1.startswith(word_2)):
            # Return an empty string 
            return ""
        # else Compare the words 
        # The comparision will go on till the len of second word
        min_len = min(len(word_1, word_2))
        for j in range(min_len):
            char1 = word_1[j]
            char2 = word_2[j]
            if(char1 != char2):
                u = char_to_indx[char1]
                v = char_to_indx[char2]
                if(v not in adj_list[u]):
                    adj_list[u].add(v)
                    in_degree[v] += 1
                break
    # Initialize the queue
    q = deque()
    # Append all the elements with indegree 0 to the queue
    for i in range(len(total_chars)):
        if(in_degree[i] == 0):
            q.append(i)
    result = []
    while(q):
        indx = q.popleft()
        # Appensing the element instead of the index to the result 
        result.append(indx_to_char[indx]) 
        
        for neighbour_indx in adj_list[indx]:
            in_degree[neighbour_indx] -= 1
            if(in_degree[neighbour_indx] == 0):
                q.append(neighbour_indx)
                
    if(len(result) != total_chars):
        return ""
    return "".join(result)
            
        
        
        