class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        c=0
        s=0
        for i in bank:
            b=i.count('1')
            if b>0 and s>0:
                c=c+(s*b)
                s=b
            elif b>0:
                s=b
        return c        
            

         
        