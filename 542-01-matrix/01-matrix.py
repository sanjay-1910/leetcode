from collections import deque
class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        rows, cols = len(grid), len(grid[0])
        distance = [[-1] * cols for _ in range(rows)]
        queue = deque()

        # Initialize queue with all '1' cells and mark their distances as 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))  # (row, col, distance)
                    distance[i][j] = 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # Right, Down, Up, Left

        # BFS Traversal
        while queue:
            i, j, dist = queue.popleft()

            for di, dj in directions:
                ni, nj = i + di, j + dj

                # Check if the new cell is valid and unvisited
                if 0 <= ni < rows and 0 <= nj < cols and distance[ni][nj] == -1:
                    distance[ni][nj] = dist + 1
                    queue.append((ni, nj, dist + 1))

        return distance

                    

        


	
        