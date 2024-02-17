class Solution(object):
    def twoSum(self, nums, target):
        ou=[]
        for i in range(0,len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ou.append(i)
                    ou.append(j)
                    return ou



        
           
        