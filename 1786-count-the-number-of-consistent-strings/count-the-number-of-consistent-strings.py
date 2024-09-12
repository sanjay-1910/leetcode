class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        d={}
        answer=0
        for i in allowed:
            d[i]=1
        for j in words:
            c=0
            for k in range(0,len(j)):
                if j[k] not in d.keys():
                    c+=1
            if c==0:
                answer+=1
        return answer
            