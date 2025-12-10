class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s=0
        l=len(nums)-1
        
        while (s<=l):
            m=(s+l)//2
            if nums[m]==target:
                return m
            elif target>nums[m]:
                s=m+1
            else:
                l=m-1
            
        return -1
        # for i in range(0,len(nums)):
        #     if nums[i]==target:
        #         return i
        # else:
        #     return -1

        