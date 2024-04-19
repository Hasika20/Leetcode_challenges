'''
200. Number of Islands
Medium

22439

509

Add to List

Share
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = 0
        lastRow, lastCol = len(grid)-1, len(grid[0])-1
        land = set((i, j) for i, row in enumerate(grid) for j, val in enumerate(row)  if val is '1')
        
        def checkAndRemove(row, col):
            if (row, col) in land:
                land.remove((row, col))
                removeAdjacent(row, col)
                
        def removeAdjacent(row, col):
            if 0 <= row <= lastRow and 0 <= col <= lastCol:
                checkAndRemove(row, col-1)
                checkAndRemove(row, col+1)
                checkAndRemove(row-1, col)
                checkAndRemove(row+1, col)
        
        if land:
            pos = land.pop()
            while pos:
                removeAdjacent(pos[0], pos[1])
                n += 1
                pos = land.pop() if land else None
        return n
        