class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        d  = {}
        one = 0
        c = 0
        for i in range(0,len(nums)):
            if nums[i] not in d.keys():
                d[nums[i]] = 1
            else:
                if(d[nums[i]] == 1):
                    one += 1
                d[nums[i]] += 1
        if one == 0:
            return 0
        for j in range(0,len(nums),3):
            c += 1
            for k in range(j,j+3):
                if(k<len(nums)):
                    d[nums[k]] -= 1
                    if(d[nums[k]] == 1):
                        one -= 1
            if one == 0:
                return c

        

        