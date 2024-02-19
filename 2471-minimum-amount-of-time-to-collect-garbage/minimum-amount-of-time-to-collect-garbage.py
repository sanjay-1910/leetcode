class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        pa=p=ma=m=gl=g=0
        n=len(garbage)
        for i in range(0,len(garbage)):
            if "P" in garbage[i]:
                p=p+(garbage[i].count("P"))
                pa=p
            if i!=n-1:
                p=p+travel[i]
            if "G" in garbage[i]:
                g=g+(garbage[i].count("G"))
                gl=g
            if i!=n-1:
                g=g+travel[i]
            if "M" in garbage[i]:
                m=m+garbage[i].count("M")
                ma=m
            if i!=n-1:
                m=m+travel[i]
        return (pa+gl+ma)


            
