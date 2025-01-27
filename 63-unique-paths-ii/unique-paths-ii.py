class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def path(obstacle,i,j,dp):
            if((i>=0 and j>=0) and obstacle[i][j] == 1):
                return 0
            if(i==0 and j==0):
                return 1
            if(i<0 or j<0):
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            left = path(obstacle,i-1,j,dp)
            right = path(obstacle,i,j-1,dp)
            dp[i][j] = left+right
            return dp[i][j]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1]*n for i in range(m)]
        return path(obstacleGrid,m-1,n-1,dp)
            