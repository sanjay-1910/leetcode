class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = 0
        odd = 0 
        even = 0
        result = 0
        MOD = 10**9+7
        for i in arr:
            prefix += i
            if prefix%2:
                odd += 1
                result = (result+1+even)%MOD
            else:
                even += 1
                result = (result+odd)%MOD
        return result
        