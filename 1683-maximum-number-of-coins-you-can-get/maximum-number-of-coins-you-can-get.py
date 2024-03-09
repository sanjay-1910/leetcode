class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles=sorted(piles,reverse=True)
        s=0
        for i in range(1,len(piles)*2//3,2):
            s=s+piles[i]
        return s
        