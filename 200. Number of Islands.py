class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row,col=len(grid),len(grid[0])
        def dfs(r,c):
            if r<0 or r==row or c<0 or c==col or grid[r][c]!="1":
                return 
            grid[r][c]="-1"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
            
        area=0
        for r in range(row):
            for c in range(col):
                if grid[r][c]=="1":
                    dfs(r,c)
                    area+=1
        return area