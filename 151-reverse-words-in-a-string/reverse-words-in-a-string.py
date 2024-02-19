class Solution:
    def reverseWords(self, s: str) -> str:
        sa=""
        fin=""
        for i in range(len(s)-1,-1,-1):
            if s[i]==" " and len(fin)==0:
                fin=fin+sa
                sa=""
            elif s[i]==" " and len(sa)!=0:
                fin=fin+" "+sa
                sa=""
            elif s[i]==" " and len(sa)==0:
                pass
            else:
                sa=s[i]+sa
        if s[0]==" ":
            return fin.strip()
        else:
            fin=fin+" "+sa
            return fin.strip()