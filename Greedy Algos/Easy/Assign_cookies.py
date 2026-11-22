def findContentChildren(self, g: list[int], s: list[int]) -> int:
        i, j, satisfied = 0, 0, 0
        # Sorting both the arrays so we can keep a track of who needs more and who needs less 
        g.sort()
        s.sort()
        while(i < len(g) and j < len(s)):
            
            if(g[i] <= s[j]):
                satisfied += 1
                i += 1
            # the cookie pointer always increases no matter we satisfy the children or not 
            j += 1
           
        return satisfied