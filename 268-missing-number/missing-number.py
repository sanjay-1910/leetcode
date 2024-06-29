class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        x=0
        y=0
        for i in range(0,len(nums)):
            x=x^nums[i]
        for j in range(1,len(nums)+1):
            y=y^j
        xo=x^y
            
        return xo
        