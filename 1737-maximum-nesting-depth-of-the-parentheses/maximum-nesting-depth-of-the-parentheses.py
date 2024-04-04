class Solution:
    def maxDepth(self, s: str) -> int:
        open=0
        depth=0
        for i in s:
            if i=='(':
                open+=1
            elif i==')':
                open-=1
            depth=max(open,depth)
        return depth
        