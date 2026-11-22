def good_numbers(n:int):
    def generate(current:list, i:int):
        if(i > len(nums) - 1):
            count += 1
            return
        generate(current, i + 1)
        current.append(nums[i])
    count = 0 # Inplace of the result array keeping track of the numbers passing our critirea
    nums = []
    current = []
    for i in range(10):
        nums.append(i)
    
    generate(current, 0)
     
    