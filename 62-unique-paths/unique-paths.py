class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(i,j,dp):
            if(i==0 and j==0):
                # dp[i][j] = 1
                return 1
            if(i<0 or j<0):
                # dp[i][j] = 0
                return 0
            if(dp[i][j] != -1):
                return dp[i][j]
            left = paths(i-1,j,dp)
            right = paths(i,j-1,dp)
            dp[i][j] = left+right
            return dp[i][j]
        dp = [[-1] * n for i in range(m)]
        return paths(m-1,n-1,dp)
        # return dp[m-1][n-1]
        