class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        prev = curr = 0
        ans = 0

        for x in nums:
            if x == 1:
                curr += 1
            else:
                ans = max(ans, prev + curr)
                prev = curr
                curr = 0

        ans = max(ans, prev + curr)

        return min(len(nums) - 1, ans)
        