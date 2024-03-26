class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m=max(nums)
        if m<0:
            return 1
        d={}
        for i in nums:
            d[i]=1
        for i in range(1,m):
            if i not in d.keys():
                return i
        return m+1
        