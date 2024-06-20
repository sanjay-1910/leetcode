
#import math
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def row(n):
            if n==2:
                return [1,1]
            ans=[1]
            po=1
            for i in range(1,n-1):
                po=po*((n-i)/i)
                ans.append(round(po))
                #po=po/i
            ans.append(1)
            return ans
        final=[[1]]
        for i in range(2,numRows+1):
            final.append(row(i))
        return final
                
            
    
        

            
