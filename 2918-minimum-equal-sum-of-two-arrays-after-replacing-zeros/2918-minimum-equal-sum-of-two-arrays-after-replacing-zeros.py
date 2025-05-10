class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        # return 12
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
        # if zeroes2 > zeroes1:
            # zeroes1,zeroes2 = zeroes2,zeroes1
        if sum2 > sum1:
            sum1,sum2 = sum2,sum1
            zeroes1,zeroes2 = zeroes2,zeroes1
        if((zeroes1+sum1) < (zeroes2+sum2)):
            return -1
        else:
            ans = zeroes1+sum1
            return ans
        