class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex==0:
            return [1]
        ans=[1]
        po=1
        rowIndex=rowIndex+1
        for i in range(1,rowIndex-1):
            po=po*(rowIndex-i)
            po=po//i
            ans.append(po)
        ans.append(1)
        return ans
    
        