from typing import List

class Solution:
    def sub(self, nums, index, prev_index, dp):
        if index == len(nums):
            return 0  # Base case: No more elements to pick
        
        # If already computed, return stored value
        if dp[index][prev_index + 1] != -1:
            return dp[index][prev_index + 1]

        # Non-Pick: Skip the current element
        non_pick = self.sub(nums, index + 1, prev_index, dp)

        # Pick: If nums[index] is greater than the last picked element
        pick = 0
        if prev_index == -1 or nums[index] > nums[prev_index]:
            pick = 1 + self.sub(nums, index + 1, index, dp)

        # Store the result in dp table and return
        dp[index][prev_index + 1] = max(pick, non_pick)
        return dp[index][prev_index + 1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n)]  # Create a 2D DP table
        return self.sub(nums, 0, -1, dp)  # Start recursion
