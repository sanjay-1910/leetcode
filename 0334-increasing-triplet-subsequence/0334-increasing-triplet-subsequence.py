class Solution:
    def rec(self, index, c, nums, prev):
            if c == 3:   # found triplet
                return True
            if index >= len(nums):  # end of array
                return False

            # pick if valid
            pick = False
            if nums[index] > prev:
                pick = self.rec(index + 1, c + 1, nums, nums[index])

            # non-pick (skip current element)
            nonpick = self.rec(index + 1, c, nums, prev)

            return pick or nonpick
    def increasingTriplet(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if self.rec(i, 1, nums, nums[i]):  # start triplet from nums[i]
                return True
        return False

        