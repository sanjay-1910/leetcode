class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = [[False]*len(grid[0]) for h in range(len(grid))]
        queue = []
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(visited[i][j] == False and grid[i][j] == 2):
                    queue.append(((i,j),0))
                    visited[i][j] = True
        ans = 0
        while(len(queue)>0):
            ii = queue[0][0][0]
            jj = queue[0][0][1]
            dist = queue[0][1]
            queue.pop(0)
            ans = max(ans,dist)
            directions = [(ii,jj+1),(ii+1,jj),(ii-1,jj),(ii,jj-1)]
            for dir in directions:
                row = dir[0]
                col = dir[1]
                if(row>=0 and col>=0 and row<len(grid) and col<len(grid[0]) and visited[row][col]==False and grid[row][col] == 1):
                    visited[row][col] = True
                    queue.append(((row,col),dist+1))
        for k in range(0,len(grid)):
            for l in range(0,len(grid[0])):
                if(visited[k][l] == False and grid[k][l]!=0):
                    return -1
        return ans
        

        