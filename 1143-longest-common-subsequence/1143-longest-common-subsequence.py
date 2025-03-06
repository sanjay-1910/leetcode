class Solution:
    def subseq(self,text1,text2,index1,index2,dp):
        if(index1 == len(text1) or index2 == len(text2)):
            return 0
        if(dp[index1][index2] != -1):
            return dp[index1][index2]
        if(text1[index1] == text2[index2]):
            dp[index1][index2] = 1+self.subseq(text1,text2,index1+1,index2+1,dp)
        else:
            left = self.subseq(text1,text2,index1+1,index2,dp)
            right = self.subseq(text1,text2,index1,index2+1,dp)
            ans = max(left,right)
            dp[index1][index2] = ans
        return dp[index1][index2]
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp= [[-1]*len(text2) for i in range(len(text1))]
        ans = self.subseq(text1,text2,0,0,dp)
        return ans
        