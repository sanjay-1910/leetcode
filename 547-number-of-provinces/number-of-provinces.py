class Solution:
    def dfs(self,i,isConnected,visited):
        visited[i] = 1
        for j in range(len(isConnected[i])):
            if(visited[j] == -1 and j!=i and isConnected[i][j]==1):
                self.dfs(j,isConnected,visited)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = 0
        visited = [-1] * len(isConnected)
        for i in range(0,len(isConnected)):
            if(visited[i] == -1):
                self.dfs(i,isConnected,visited)
                count += 1
        return count


        