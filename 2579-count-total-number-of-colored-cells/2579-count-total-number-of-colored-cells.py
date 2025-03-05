class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        sum=1
        for i in range(1,n):
            sum=sum+(4*i)
        return sum

        