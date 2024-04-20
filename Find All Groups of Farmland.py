class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows,cols = len(land),len(land[0])
        dirns = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or land[r][c] == 0 :
                return [0,0]

            land[r][c] = 0
            res = [r,c]     # bottom right 
            for dr,dc in dirns :
                newR,newC = r+dr, c+dc
                curr = dfs(newR,newC)
                res[0] = max(res[0],curr[0])
                res[1] = max(res[1],curr[1])
            return res                


        res = []
        for r in range(rows):
            for c in range(cols):
                if land[r][c] == 1 :
                    bottomRight = dfs(r,c)
                    res.append( [r,c]+bottomRight )
        return res