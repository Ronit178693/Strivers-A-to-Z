'''
    For the XOR operator it gives 1 only when it 1-0 or 0-1 when both the bits are same it gives 0
    '''
def minBitFlips( start: int, goal: int) -> int:
        # So doing XOR on both the numbers finds out only the bits which were different 
        n = start ^ goal
        # That  is the case when the start and goal are already same
        if(n == 0):
            return 0
        count = 1
        while(n != 1):
            remainder = n % 2
            if(remainder == 1):
                count += 1
            n = n//2
        return count