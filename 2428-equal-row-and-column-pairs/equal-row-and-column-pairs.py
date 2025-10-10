class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        rows = []
        cols = {}
        for i in range(0,len(grid)):
            rows.append(grid[i])
            for j in range(0,len(grid[0])):
                if j not in cols.keys():
                    cols[j] = [grid[i][j]]
                else:
                    cols[j].append(grid[i][j])
        columns = [x for x in cols.values()]
        count = 0
        for row in rows:
            for col in columns:
                if row == col:
                    count += 1
        
        return count








        