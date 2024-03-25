class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        l=[]
        for i in arr:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for i in d.keys():
            l.append(d[i])
        s=list(set(l))
        if len(s)==len(l):
            return True
        else:
            return False

        
        
        