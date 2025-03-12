class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dp(n):  
            # write down base cases
            if n < 2: 
                return cost[n] 
            if(dplist[n] != -1):
                return dplist[n]
            else:
            # write recursive function based on what you can change (climb one or two steps)
            # return cost[n] + min(dp(n-1), dp(n-2))
                dplist[n]=cost[n]+min(dp(n-1),dp(n-2))
                return dplist[n]
		
		# since we want to know the min cost to get to the final step, we use the code below 
        length = len(cost) 
        dplist = [-1]*length
        return min(dp(length-1), dp(length-2))


        