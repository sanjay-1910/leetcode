class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        i = 0
        c = 0
        ko = 1
        j = 1
        while(j<len(colors)+k and i<len(colors)):
            jj = j%len(colors)
            if(colors[jj]!=colors[jj-1]):
                ko += 1
            else:
                i = jj
                ko = 1
            if(j-i+1)==k:
                # if(j<len(colors)) and colors[i] == colors[jj]:
                # if(colors[i] == colors[jj]):
                c+=1
                i+=1
                ko-=1   
            j+=1
        return c
        










                        # else:
                #     # val = if (jj%len(colors)-1 >0) ? jj%len(colors)-1 : len(colors)-jj%len(colors)-1 >0
                #     val = (jj % len(colors) - 1) if (jj % len(colors) - 1 > 0) else (len(colors) - jj % len(colors) - 1)
                #     if colors[i] == colors[val]:
                #         c+=1
                #         i+=1
                #         ko-=1