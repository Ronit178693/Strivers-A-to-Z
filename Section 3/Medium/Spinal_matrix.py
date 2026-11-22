# Optimal Solution
def Spinal(matrix:list):
        Right = len(matrix[0]) - 1
        left = 0
        top = 0
        bottom = len(matrix) - 1
        ans = []
        while left <= Right and top <= bottom:
            for i in range(left, Right + 1):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom + 1):
                ans.append(matrix[i][Right])
            Right -= 1
            if (
                top <= bottom
            ):  # These conditions are for the cases when there are only a row or only a column left

                for i in range(Right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
            if left <= Right:

                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans


'''
TC - O(N^2)
SC - O(1)
'''

