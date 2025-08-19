class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i = 0
        ans = 0
        while(i<len(nums)):
            if(nums[i] == 0):
                # ans = 0/
                su = 0   
                while(i < len(nums) and nums[i] == 0):
                    su += 1
                    ans += su
                    i+=1
            i+=1
        return ans     