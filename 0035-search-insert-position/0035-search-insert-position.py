class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return 0
        f=0
        l=len(nums)-1
        while(f<=l):
            m=(f+l)//2
            if nums[m]==target:
                return m
            elif nums[m]>target:
                l=m-1
            else:
                f=m+1
        return f
        