class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sumo = 0
        count = 0
        d = {0:1}  # Initialize the dictionary with sum 0 having one count

        for i in range(len(nums)):
            sumo += nums[i]
            if sumo - k in d:
                count += d[sumo - k]
            if sumo in d:
                d[sumo] += 1
            else:
                d[sumo] = 1

        return count

                
                
                
        