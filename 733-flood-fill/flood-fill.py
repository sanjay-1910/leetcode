class Solution:
    def dfs(self,image,sr,sc,original,color,visited):
        n = len(image)
        m = len(image[0])
        visited[sr][sc] = color
        directions = [[sr-1,sc],[sr+1,sc],[sr,sc-1],[sr,sc+1]]
        for nrow,ncol in directions:
            if(nrow>=0 and ncol>=0 and nrow<n and ncol<m and visited[nrow][ncol] == original):
                self.dfs(image,nrow,ncol,original,color,visited)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = image
        original = image[sr][sc]
        if(original!=color):
            self.dfs(image,sr,sc,original,color,visited)
        return visited





        