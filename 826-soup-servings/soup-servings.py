class Solution:
    def soupServings(self, n: int) -> float:
        if n > 4800:  # experimentally found cutoff for 1e-5 accuracy
            return 1.0

        from functools import lru_cache

        # Convert to units of 25 mL
        N = (n + 24) // 25  # ceil(n / 25)

        @lru_cache(None)
        def dp(a, b):
            # Base cases
            if a <= 0 and b <= 0:
                return 0.5  # both empty same time
            if a <= 0 and b > 0:
                return 1.0  # A empty first
            if b <= 0 and a > 0:
                return 0.0  # B empty first

            # Expected probability from current state
            return 0.25 * (
                dp(a - 4, b) +
                dp(a - 3, b - 1) +
                dp(a - 2, b - 2) +
                dp(a - 1, b - 3)
            )

        return dp(N, N)
        