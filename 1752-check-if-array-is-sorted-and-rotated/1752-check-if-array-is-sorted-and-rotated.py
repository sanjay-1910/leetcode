class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        n=len(nums)
        for i in range(1,n):
            if(nums[i-1]>nums[i]):
                c+=1
        if nums[n-1]>nums[0]:
            c+=1
        return c<=1
        


            
        