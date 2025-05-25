# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = (10**9) + 7
        memo = {}  # Dictionary to store computed values
        
        def dfs(current_len):
            # Base case: if the current length exceeds the high limit, return 0
            if current_len > high:
                return 0
            
            # If the result for this length is already computed, return it from memo
            if current_len in memo:
                return memo[current_len]
            
            # If current_len is between low and high, it's a valid good string
            count = 0
            if low <= current_len <= high:
                count = 1
            
            # Recurse with appending zero `0`s and one `1`s
            count += dfs(current_len + zero)  # Adding `zero` number of 0s
            count += dfs(current_len + one)   # Adding `one` number of 1s
            
            # Store the result in the memo dictionary
            memo[current_len] = count % MOD
            
            return memo[current_len]
        
        # Start the recursion with an empty string (length 0)
        return dfs(0)