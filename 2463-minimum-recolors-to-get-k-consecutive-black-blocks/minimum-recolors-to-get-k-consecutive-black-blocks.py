class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = 0
        c = 0
        for i in range(0,k):
            if(blocks[i] == 'W'):
                c+=1
        ans = c
        for j in range(k,len(blocks)):
            if(blocks[j-k]=='W'):
                c-=1
            if(blocks[j] == 'W'):
                c+=1
            ans = min(ans,c)
        return ans
        
        