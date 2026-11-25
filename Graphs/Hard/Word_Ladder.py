from collections import deque
def ladder(beginWord, endWord, wordList):
    # Initially convert the given wordlist to a set for fast lookups 
    wordList_set = set(wordList)
    # Edge case - The startWord can be present in the wordList so we will remove it from the list 
    if(beginWord in wordList_set):
        wordList_set.remove(beginWord)
    # Initializing the queue
    q = deque()
    # Appending the start word insied the queue with the tree height 
    q.append((beginWord, 1))
    # As the start word is not present in the word list we dont have to rempove it from the set 
    while(q):
        # Popping out the word and the heigh of the tree at that perticular point 
        word, height = q.popleft()
        # Iterating through each char of the word
        if(word == endWord):
            return height
        for i in range(len(word)):
            original_char = word[i]
            # looping through all the letters for finding the replacement
            for letter in range(ord('a'), ord('z') + 1):
                # Now if the new word formed is not in the dictonary we completely ignore the new word but if it is in the dictonary we apppend it to the queue with the updated height 
                
                # Updating the perticular char
                new_word = word[:i] + chr(letter) + word[i + 1:]
                # If the word is present in the set 
                if(new_word in wordList_set):
                    # Remove the word from the set 
                    wordList_set.remove(new_word)
                    q.append((new_word, height + 1))
    return 0
                    
                
        