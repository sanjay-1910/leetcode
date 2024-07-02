class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        i=0
        j=0
        l=[]
        nums1.sort()
        nums2.sort()
        while(i<len(nums1) and j<len(nums2)):
            if nums1[i]==nums2[j]:
                l.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:
                i+=1
            else:
                j+=1
        return l
                

        