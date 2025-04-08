class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = nums1[:m]
        list(map(lambda x: nums1.append(x), nums2)) 
        nums1.sort(key=lambda x:x)