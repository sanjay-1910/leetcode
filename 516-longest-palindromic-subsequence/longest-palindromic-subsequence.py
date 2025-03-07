class Solution:
    def seq(self,i,j,s,dp):
        if(i==j):
            return 1
        if(i>j):
            return 0
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i] == s[j]):
            dp[i][j] = 2+self.seq(i+1,j-1,s,dp)
        else:
            left = self.seq(i+1,j,s,dp)
            right = self.seq(i,j-1,s,dp)
            ans = max(left,right)
            dp[i][j] = ans
        return dp[i][j]

    def longestPalindromeSubseq(self, s: str) -> int:
        dp =[[-1]*len(s) for i in range(len(s))]
        return self.seq(0,len(s)-1,s,dp)


