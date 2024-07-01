class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c=0
        for i in range(0,len(arr)):
            if arr[i]%2!=0 and c==2:
                return True
            elif arr[i]%2!=0:
                c+=1
            else:
                c=0
        return False
                
                
        