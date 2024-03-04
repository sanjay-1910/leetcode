class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        score=0
        mscore=0
        i=0
        j=len(tokens)-1
        while(i<=j):
            if(tokens[i]<=power):
                power=power-tokens[i]
                score=score+1
                i=i+1
                mscore=max(mscore,score)
            elif(score>=1):
                power=power+tokens[j]
                j=j-1
                score=score-1
            else:
                i=i+1
        return mscore

        
        