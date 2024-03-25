class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        d={}
        l=[]
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                l.append(i)
        return l
        