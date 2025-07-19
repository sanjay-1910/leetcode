class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        i=0
        res=[]
        while i!=len(folder):
            res.append(folder[i])
            i+=1
            while i!=len(folder) and res[-1] in folder[i]:
                if (folder[i][len(res[-1])]) !="/" or folder[i].index(res[-1])!=0:
                    break
                i+=1
        return res
        