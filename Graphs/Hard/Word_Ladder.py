from collections import deque
def ladder(beginWord, endWord, wordList):
    # Initially convert the given wordlist to a set for fast lookups 
    wordList_set = set(wordList)
    # Initializing the queue
    q = deque()
    # Appending the start word insied the queue with the tree height 
    q.append((beginWord, 1))
    # As the start word is not present in the word list we dont have to rempove it from the set 
    while(q):
        # Popping out the word and the heigh of the tree at that perticular point 
        word, height = q.popleft()
        for 
        