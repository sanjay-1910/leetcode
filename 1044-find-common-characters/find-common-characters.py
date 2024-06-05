class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d={}
        l=[]
        for i in words[0]:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for i in range(1,len(words)):
            e={}
            for j in words[i]:
                if j in d.keys():
                    if j in e.keys() and e[j]<d[j]:
                        e[j]+=1
                    if j not in e.keys():
                        e[j]=1
            d=e
        for i in d.keys():
            for j in range(0,d[i]):
                l.append(i)
        return l
            


        
        
                                                       
        