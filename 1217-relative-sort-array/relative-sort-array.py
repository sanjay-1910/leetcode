class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        final=[]
        fi=[]
        for i in arr1:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        for i in arr2:
            final.extend([i]*d[i])
            d[i]=0
        for i in d.keys():
            if d[i]>0:
                fi.extend([i]*d[i])
        fi.sort()
        final.extend(fi)
        return final
        
        
        