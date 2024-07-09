class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # def prefix(t,i):
        #     for j in range(0,i):
        #         if t in d.keys():
        #             return d[t]
        #     else:
        #         return -1
        # sumo=0
        # count=0
        # d={}
        # for i in range(0,len(nums)):
        #     sumo=sumo+nums[i]
        #     d[sumo]=i
        #     if sumo==k:
        #         count+=1
        #     elif sumo>k:
        #         t=(sumo-k)
        #         if prefix(t,i)>=0:
        #             count+=1
        #     elif k==0:
        #         if nums[i]==0:
        #             count+=1
        #         elif nums[i]<0:
        #             t=sumo
        #             if prefix(t,i)>=0:
        #                 count+=1
        # return count
        sumo = 0
        count = 0
        d = {0: 1}  # Initialize the dictionary with sum 0 having one count

        for i in range(len(nums)):
            sumo += nums[i]

            # Check if (sumo - k) is in the dictionary
            if sumo - k in d:
                count += d[sumo - k]

            # Add sumo to the dictionary
            if sumo in d:
                d[sumo] += 1
            else:
                d[sumo] = 1

        return count

                
                
                
        