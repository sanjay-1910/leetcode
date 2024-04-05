class Solution:
    def makeGood(self, s: str) -> str:
        def dop(c, aa):
            l = list(aa)
            a = ""
            i = 0
            while i < len(l) - 1:
                if ord(l[i]) - ord(l[i + 1]) != 32 and ord(l[i + 1]) - ord(l[i]) != 32:
                    a = a + l[i]
                    i = i + 1
                else:
                    i = i + 2
                    c = c + 1
            if i == len(l)-1:
                a = a + l[i]
            if c != 0:
                return dop(0, a)
            #elif i == len(l)-1:
                #a = a + l[i]
            return a
        return dop(0, s)


                

        