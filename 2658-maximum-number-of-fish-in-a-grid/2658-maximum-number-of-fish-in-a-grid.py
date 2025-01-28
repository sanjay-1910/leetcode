class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i,j,grid,dp):
            if(dp[i][j]!=-1):
                return dp[i][j]
            queue = [(i,j)]
            visited = set()
            visited.add((i,j))
            cost = grid[i][j]
            grid[i][j] = 0
            # directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
            while(len(queue)!=0):
                ni,nj = queue.pop(0)
                directions = [[ni-1,nj],[ni+1,nj],[ni,nj-1],[ni,nj+1]]
                for dir in directions:
                    ni,nj = dir
                    if(ni<0 or nj<0 or ni>=len(grid) or nj==len(grid[0]) or grid[ni][nj]==0):
                        continue
                    else:
                        if((ni,nj) not in visited):
                            cost+=dfs(ni,nj,grid,dp)
                            visited.add((ni,nj))
                            queue.append((ni,nj))
            dp[i][j] = cost
            return cost
        dp = [[-1]*len(grid[0]) for i in range(len(grid))]
        final = 0
        for i in range(0,len(grid)):
            ans = 0
            for j in range(0,len(grid[i])):
                if(grid[i][j] != 0):
                    ans = dfs(i,j,grid,dp)
                final = max(ans,final)
        return final

                
                

        