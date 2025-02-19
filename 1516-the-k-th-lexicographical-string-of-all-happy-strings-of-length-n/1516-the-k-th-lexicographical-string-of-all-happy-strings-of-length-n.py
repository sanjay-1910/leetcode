class Solution:
    def generate_string(self,n,k,ans,length,final,alphabets):
        if(length == n):
            final.append("".join(ans))  # Correct way
            return
        for i in alphabets:
            if(ans):
                if(ans[-1] != i):
                    ans.append(i)
                    self.generate_string(n,k,ans,length+1,final,alphabets)
                    ans.pop()
            else:
                ans.append(i)  # Modify ans in place
                self.generate_string(n, k, ans, length + 1, final, alphabets)  # Recursive call
                ans.pop()  # Backtrack

    def getHappyString(self, n: int, k: int) -> str:
        final = []
        alphabets = ['a','b','c']
        ans = []
        self.generate_string(n,k,ans,0,final,alphabets)
        final.sort()
        if(k>len(final)):
            return ""
        return final[k-1]
        