# Brute Force Solution 
# All the cards must get utilized in the given array 
def hands(hand, groupSize):
    if(len(hands) % groupSize != 0):
        return False
    hand.sort()
    visited = [False] * len(hand)
    for i in range(len(hands)):
        for j in range(i, len(hands)):
            
    
    