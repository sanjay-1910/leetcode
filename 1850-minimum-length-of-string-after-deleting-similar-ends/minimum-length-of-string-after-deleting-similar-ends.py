class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        sa=""
        while(i<j):
            if(s[i]==s[j]):
                sa=s[i]
                i=i+1
                j=j-1
            elif(s[i]==sa):
                i=i+1
            elif(s[j]==sa):
                j=j-1
            else:
                return (j+1)-i
        if((i==j and s[i]==sa) or i>j):
            return 0
        else:
            return 1
            
        