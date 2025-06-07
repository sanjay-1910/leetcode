class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        zeroes1 = 0
        zeroes2 = 0
        sum1 = 0
        sum2 = 0
        for i in range(0,len(nums1)):
            if nums1[i] == 0:
                zeroes1 += 1
            sum1 += nums1[i]
        for j in range(0,len(nums2)):
            if(nums2[j] == 0):
                zeroes2 += 1
            sum2 += nums2[j]
        if(sum1 == sum2):
            if (zeroes1 == 0) != (zeroes2 == 0):
                return -1
            return sum1+max(zeroes1,zeroes2)
        if(sum2 > sum1):
            sum1,sum2 = sum2,sum1
            zeroes1,zeroes2 = zeroes2,zeroes1
        if(zeroes2 == 0 or ((zeroes2+sum2)>(zeroes1+sum1) and zeroes1==0)):
            return -1
        else:
            return max(zeroes1+sum1,zeroes2+sum2)
        