class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # s=0
        # l=len(nums)-1
        # p=0
        # while True:
        #     m=(s+l)//2
        #     if nums[m]>0 and nums[m-1]<=0:
        #         p=m
        #         break
        #     if nums[m]<0:
        #         s=m
        #     if nums[m]>0:
        #         l=m
        #     if min(nums)>=0:
        #         return len(nums)-nums.count(0)
        #     if max(nums)<=0:
        #         return len(nums)-nums.count(0)
        # return max(p,(len(nums)-p-nums.count(0)))
        pos = 0
        neg = 0
        for i in range(len(nums)):
            if(nums[i] < 0):
                neg += 1
            if(nums[i] > 0):
                pos += 1
        return max(pos,neg)
        
    
        

        