class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        ans = 0
        dp = [[0]*len(mat[0]) for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    # build height like a histogram
                    dp[i][j] = 1 + (dp[i-1][j] if i > 0 else 0)

                    # now extend left and take min-height to count rectangles
                    min_height = dp[i][j]
                    for k in range(j, -1, -1):  # move left
                        if dp[i][k] == 0:
                            break
                        min_height = min(min_height, dp[i][k])
                        ans += min_height
        return ans

        # 1 0 1
        # 2 3 0
        # 3 7 0




        