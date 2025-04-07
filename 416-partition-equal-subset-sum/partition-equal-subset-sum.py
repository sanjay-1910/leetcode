from typing import List

class Solution:
    def equal(self, nums, subset_sum, i, target, dp):
        if subset_sum > target:
            return False
        if subset_sum == target:
            return True
        if i == len(nums):
            return False
        if dp[i][subset_sum] != -1:
            return dp[i][subset_sum]

        # Include the current number
        include = self.equal(nums, subset_sum + nums[i], i + 1, target, dp)
        # Exclude the current number
        exclude = self.equal(nums, subset_sum, i + 1, target, dp)

        dp[i][subset_sum] = include or exclude
        return dp[i][subset_sum]

    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]
        return self.equal(nums, 0, 0, target, dp)
