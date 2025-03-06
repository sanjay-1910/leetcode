class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        d = {}
        sum = 0
        ans = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if grid[i][j] not in d:
                    d[grid[i][j]] = 1
                    sum += grid[i][j]
                else:
                    ans.append(grid[i][j])
        n = n*n
        total_sum = (n*(n+1))//2
        ans.append(total_sum - sum)
        return ans
        

        
        # ans.append(xor)
