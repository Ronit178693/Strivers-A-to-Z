def myPow(self, x: float, n: int) -> float:
        '''
        Case 1) n is positive

        Case 2) n is negative
        '''
        if(n == 0):
            return 1
        if (n == 1):
            return x

        if(n > 0):
            if(n%2 == 0):
                return self.myPow(x*x, n//2)
            return x*self.myPow(x, n-1)
        elif(n < 0):
            x = 1/x
            n = abs(n)
            return self.myPow(x, n)