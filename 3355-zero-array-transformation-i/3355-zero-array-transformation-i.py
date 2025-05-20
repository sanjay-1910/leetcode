class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        sumarray = [0]*(len(nums)+1)
        for i in queries:
            sumarray[i[0]] -= 1
            sumarray[i[1]+1] += 1
        leftsub = 0
        for j in range(0,len(sumarray)-1):
            sumarray[j] = leftsub+sumarray[j]
            leftsub = sumarray[j]
            if(nums[j]+sumarray[j] > 0):
                return False
        return True