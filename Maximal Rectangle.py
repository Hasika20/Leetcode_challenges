'''85. Maximal Rectangle
Hard

9822

169

Add to List

Share
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = [["0"]]
Output: 0
Example 3:

Input: matrix = [["1"]]
Output: 1
 

Constraints:

rows == matrix.length
cols == matrix[i].length
1 <= row, cols <= 200
matrix[i][j] is '0' or '1'.'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        no_of_rows = len(matrix)
        no_of_columns = len(matrix[0])
        area = 0
        height = [0] * (no_of_columns + 1)
        for i in range(no_of_rows):
            for j in range(no_of_columns):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0
            stack = [-1]
            for j in range(no_of_columns + 1):
                while height[j] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = j - stack[-1] - 1
                    area = max(area, h * w)
                stack.append(j)
        return area
