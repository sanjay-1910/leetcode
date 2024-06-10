class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count=0
        temp=heights
        heights=sorted(heights)
        for i in range(0,len(heights)):
            if temp[i]!=heights[i]:
                count=count+1
        return count


            
        