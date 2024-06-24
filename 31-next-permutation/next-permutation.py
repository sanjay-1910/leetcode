class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        brea=-1
        for i in range(n-2,-1,-1):
            if nums[i]<nums[i+1]:
                brea=i
                break
        if brea==-1:
            nums.reverse()
            return nums
        for i in range(n-1,brea,-1):
            if nums[i]>nums[brea]:
                temp=nums[i]
                nums[i]=nums[brea]
                nums[brea]=temp
                break
        nums[brea+1: ]=nums[n-1:brea:-1]
        return nums
                
                
        