class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        ans=0
        d={'a':0,'b':0,'c':0}
        for r,c in enumerate(s):
            d[c]+=1
            while all(i>0 for i in d.values()):
                ans+=len(s)-r
                d[s[l]]-=1
                l+=1
        return ans                