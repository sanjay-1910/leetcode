class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        t=[nums[0]]
        for i in range(1,len(nums)):
            b=t[i-1]+nums[i]
            t.append(b)
        s=t[-1]
        ta=0
        for i in range(0,len(t)):
            s=s-nums[i]
            if s==ta:
                return i
            ta=ta+nums[i]
        return -1

            



        

            



        