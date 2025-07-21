class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = s[0]
        prev = s[0]
        c = 1
        for i in range(1,len(s)):
            if(s[i] == prev):
                if(c<2):
                    ans += s[i]
                    c+=1
            else:
                ans += s[i]
                c = 1
                prev = s[i]
        return ans


            
        