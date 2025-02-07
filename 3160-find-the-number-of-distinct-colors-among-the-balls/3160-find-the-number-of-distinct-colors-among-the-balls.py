class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        c = 0
        ans = []
        balls = {}
        colors = {}
        for i in range(0,len(queries)):
            if(queries[i][0] not in balls.keys() or balls[queries[i][0]]==0):
                balls[queries[i][0]] = queries[i][1]
                if(queries[i][1] not in colors.keys() or colors[queries[i][1]] == 0):
                    c += 1
                    colors[queries[i][1]] = 1
                else:
                    colors[queries[i][1]] += 1
            else:
                if(balls[queries[i][0]] != queries[i][1]):
                    if(queries[i][1] not in colors.keys() or colors[queries[i][1]]==0):
                        c+=1
                        colors[queries[i][1]] = 1  
                    else:
                        colors[queries[i][1]] += 1  
                    actual = balls[queries[i][0]]
                    if(colors[actual] == 1):
                        c-=1
                        colors[actual]-=1
                    else:
                        colors[actual]-=1

                    balls[queries[i][0]] = queries[i][1]
            ans.append(c)
        return ans
        
            


        