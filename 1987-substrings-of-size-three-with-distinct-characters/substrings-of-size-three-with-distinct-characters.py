class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        if(len(s)<3):
            return 0
        d = {}
        c = 0
        for i in range(0,3):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        if(len(d)==3):
            c+=1
        for j in range(3,len(s)):
            d[s[j-3]] -= 1
            if(s[j] not in d):
                d[s[j]] = 1
            else:
                d[s[j]] += 1
            if(d[s[j-3]] == 0):
                del d[s[j-3]]
            if(len(d) == 3):
                c+=1
        return c

        