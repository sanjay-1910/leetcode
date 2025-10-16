class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max=prices[-1]
        l=[]
        for i in range(len(prices)-1,-1,-1):
            if prices[i]>max:
                max=prices[i]
            l.append(max)
        l.reverse()
        fin=0
        fin1=0
        for i in range(0,len(prices)-1):
            if l[i+1]>prices[i]:
                fin1=l[i+1]-prices[i]
                if fin1>fin:
                    fin=fin1
        return fin
                

        