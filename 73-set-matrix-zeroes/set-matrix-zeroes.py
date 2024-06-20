class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        d={}
        e={}
        p=len(matrix[0])
        for i in range(0,len(matrix)):
            for j in range(0,p):
                if(matrix[i][j]==0):
                    d[i]=1
                    e[j]=1
        for i in range(0,len(matrix)):
            for j in range(0,p):
                if i in d.keys():
                    matrix[i]=[0]*p
                elif j in e.keys():
                    matrix[i][j]=0
                                    
        
        