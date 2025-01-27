class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def paths(i,j):
            if(i==0 and j==0):
                return 1
            if(i<0 or j<0):
                return 0
            left = paths(i-1,j)
            right = paths(i,j-1)
            return left+right
        result = paths(m-1,n-1)
        return result
        