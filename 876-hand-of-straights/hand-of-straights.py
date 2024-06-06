class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        d=Counter(hand)
        for i in hand:
            if i in d.keys() and d[i]>0:
                d[i]-=1
                for j in range(1,groupSize):
                    if d[i+j]>0:
                        d[i+j]-=1
                    else:
                        return False
        return True

        
                
         
