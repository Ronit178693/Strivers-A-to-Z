# Brute force solution using sliding window solution of size 2 
def collision(nums):
    if(len(nums) == 1 or len(nums) == 0):
        return nums
    i = 0
    while(i < len(nums) - 1):
        # Collision only happens if the left element moves to the right and the right moves to the left 
        # Nothing happens when then left moves to left and right moves to right 
        if(nums[i] > 0 and nums[i+1] < 0):
            left_astroid = nums[i]
            right_astroid = abs(nums[i + 1])
            # After finding the conflicting astroids compare their sizes for collision 
            if(left_astroid > right_astroid):
                nums.pop(i + 1)
            elif(left_astroid < right_astroid):
                nums.pop(i)
            # When both elements are of same size
            else:
                # Removing the right element shrinks the size of the list instead of changing the indexes by shifting the elements 
                nums.pop(i + 1)
                nums.pop(i)
            # Resetting the value of i for re computation 
            i = 0   
        else:
            i += 1
    return nums 


# Optimal Solution using monotonic stack 
'''
Stck is being used here because the problem occures when the astroids are moving in opposite directions and and we have to keep a track of all the last appended positive signed astroids to compare them with the negative signed astroid found

'''

def collision(nums):
    st = []
    for i in range(len(nums)):
        # If the only astroids we are encountering are moving right
        if(nums[i] > 0):
            st.append(nums[i])
        # If the elements are moving left
        else:
            # when we first encounter the left moving astroid we collide it with all the astroids moving right 
            while(st and st[-1] < abs(nums[i]) and st[-1] > 0):
                st.pop()
            # When the stack is not empty and the astroids moving left and right are of same size
            if(st and st[-1] == abs(nums[i])):
                st.pop()
            elif(not st or st[-1] < 0):
                st.append(nums[i])
    return st
                
               
                    
     
    
        
        
    