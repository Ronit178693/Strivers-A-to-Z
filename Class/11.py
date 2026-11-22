# Brute Force 
def maxArea(self, height: list[int]) -> int:
          Max_water = float('-inf')
          for i in range(len(height)):
              for j in range(1, len(height)):
                  length = min(height[i], height[j])
                  bredth = j-i
                  area = length * bredth
                  Max_water = max(Max_water, area)
          return Max_water
      
'''
TC - O(N^2)
SC - O(1)
'''
   


def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        Max_area = float('-inf')
        while(j > i):
            if(height[j] > height[i]):
                length = height[i]
                bredth = j - i
                area = length * bredth
                Max_area = max(area, Max_area)
                i += 1
            elif(height[j] == height[i]):
                length = height[i]
                bredth = j - i
                area = length * bredth
                Max_area = max(area, Max_area)
                j -= 1
            else:
                length = height[j]
                bredth = j - i
                area = length * bredth
                Max_area = max(area, Max_area)
                j -= 1
        return Max_area
    
'''
TC - O(N)
SC - O(1)
'''
