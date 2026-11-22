def hammingWeight(n: int) -> int:
        count = 1
        while(n != 1):
            remainder = n % 2
            if(remainder == 1):
                count += 1
            n = n//2
        return count