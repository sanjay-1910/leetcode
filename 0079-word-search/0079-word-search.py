class Solution:
    def bfs(self,i,j,board,visited,m,n,word,index):
        if(index == len(word)-1):
            return True
        visited[i][j] = True
        directions = [[i-1,j],[i+1,j],[i,j-1],[i,j+1]]
        for dir in directions:
            ni,nj = dir
            if(ni>=0 and nj>=0 and ni<m and nj<n and visited[ni][nj] == False and board[ni][nj] == word[index+1]):
                if(self.bfs(ni,nj,board,visited,m,n,word,index+1)):
                    return True
        visited[i][j] = False
        return False
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]       # 
        for i in range(0,len(board)):
            for j in range(0,len(board[0])):
                if(board[i][j] == word[0]):
                    if(self.bfs(i,j,board,visited,m,n,word,0)):
                        return True
        return False
        