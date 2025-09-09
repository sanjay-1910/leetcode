class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = second = float('inf')

        for n in nums:
            if n <= first:
                first = n  # update smallest
            elif n <= second:
                second = n  # update second smallest
            else:
                return True  # found a number bigger than both -> triplet exists
        
        return False
        