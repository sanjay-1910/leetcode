class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        last_non_zero = 0
        for i in range(0,len(nums)):
            if(nums[i]!=0):
                nums[i],nums[last_non_zero] = nums[last_non_zero],nums[i]
                last_non_zero += 1

            



        