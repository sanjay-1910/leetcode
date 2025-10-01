class Solution(object):
    def threeSum(self, nums):
        final=[]
        nums.sort()
        for i in range(0,len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    final.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[right]==nums[right-1]:
                        right=right-1
                    while left<right and nums[left]==nums[left+1]:
                        left=left+1
                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        return final
            
                    