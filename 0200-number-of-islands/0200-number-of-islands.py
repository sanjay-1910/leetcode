class Solution:
    def dfs(self,row,col,grid,ans):
        n = len(grid)
        m = len(grid[0])
        ans[row][col] = 1
        directions = [[row,col-1],[row,col+1],[row-1,col],[row+1,col]]
        for nrow,ncol in directions:
            # nrow,ncol = direction
            if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and ans[nrow][ncol] == -1 and grid[nrow][ncol] =="1"):
            # if(ans[nrow][ncol] == -1):
                self.dfs(nrow,ncol,grid,ans)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ans = [[-1]*len(grid[0]) for i in range(len(grid))]
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(ans[i][j] == -1 and grid[i][j] =="1"):
                    count += 1
                    self.dfs(i,j,grid,ans)
        return count
        