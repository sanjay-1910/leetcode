class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n,1,-1):
            ans=[]
            for i in range(0,len(nums)-1):
                d=nums[i]+nums[i+1]
                ans.append(d%10)
            nums=ans
        return nums[0]
        