# Brute Force Solution using Recursion
'''
All the recursive problems asking to generate all the pairs, substets or combinations are solved using the decision tree method

1) Decide the states of the function i.e. current to store the result of a brunch in recursion tree and i to point an element 

2) At index i the rest of the problem will be solved perfectly we just have to make a choice for that specific index

3) Hitting the base condition 


Because of pass-by-reference, you are not saving what is inside current at that exact second. Instead, you are giving the result list a direct pointer to the current list.Since current keeps changing as elements are appended and popped, all the entries inside result change along with it. By the very end of the program, current is popped all the way back to being completely empty []. Therefore, your entire result list becomes a collection of empty lists
'''
def power_set(nums:list) -> list[list[int]]:
    def generate(current:list, i:int = 0):
        if(i > len(nums) - 1):
            result.append(current[:]) # Fix : Was passing the pointer pointing to current now taking a snapshort of the list and appending it in the result list
            return 
        generate(current, i + 1)
        current.append(nums[i])
        generate(current, i + 1)
        current.pop()
        
    result = []
    current = []
    generate(current, 0)
    return result

'''
TC - O((2^N)*N) - As each list will have 2^n subsets so for every substring we are performing n operations keeping the buffet example in mine we are moving through the buffet 2^n times 

SC - The active memory uses (O(n) for the call stack and (O(n) for the current path array (combining to (O(n)), while the output array grows to hold all 2^{n} subsets.
'''
