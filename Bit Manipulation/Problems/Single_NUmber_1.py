def singleNumber( nums: list[int]) -> int:
        # XOR of an element with the same element returns 0, eg. 3^3 = 0 so the intution is if every number appears twice then only one number appears once then the XOR of all the elements in the array must be equal to the number that appears once 

        XOR = 0
        for i in range(len(nums)):
            XOR = XOR ^ nums[i] #Starting with 0^nums[i] = arr[i]{property} then from next iteration we get arr[i]^arr[i+1]
        return XOR