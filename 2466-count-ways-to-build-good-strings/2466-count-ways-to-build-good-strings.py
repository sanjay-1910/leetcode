# # class Solution:
# #     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
# #         def good_strings(s, low, high, zero, one,count):
# #             if len(s) > high:  # Base case: if string length exceeds `high`, stop recursion
# #                 return 0
            
# #             # Count the current string if its length is within the range [low, high]
# #             # count = 0
# #             if low <= len(s) <= high:
# #                 count += 1
            
# #             # Generate new strings by appending `zero` zeros or `one` ones
# #             zero_string = "0" * zero
# #             one_string = "1" * one
            
# #             good_strings(s + zero_string, low, high, zero, one,count)
# #             good_strings(s + one_string, low, high, zero, one,count)
# #             MOD=(10**9)+7
# #             return count%MOD
        
# #         # Start recursion with an empty string
# #         return good_strings("", low, high, zero, one,0)
# # class Solution:
# #     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
# #         MOD = (10**9) + 7  # To handle large numbers

# #         def good_strings(s_length, low, high, zero, one):
# #             if s_length > high:  # Base case: if string length exceeds `high`, stop recursion
# #                 return 0
            
# #             # Count the current string if its length is within the range [low, high]
# #             count = 1 if low <= s_length <= high else 0
            
# #             # Recursively calculate counts for adding zero_string and one_string
# #             count += good_strings(s_length + zero, low, high, zero, one)
# #             count += good_strings(s_length + one, low, high, zero, one)
            
# #             return count % MOD  # Return count modulo MOD
        
# #         # Start recursion with an initial string length of 0
# #         return good_strings(0, low, high, zero, one)

# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         # Declare `c` as a global variable
#         global c
#         MOD = (10**9) + 7
        
#         def good_strings(s, low, high, zero, one):
#             global c  # Access the global variable `c`
#             if len(s) > high:  # Base case: if string length exceeds `high`, stop recursion
#                 return
            
#             # Increment `c` if the current string is within the range [low, high]
#             if low <= len(s) <= high:
#                 c += 1
            
#             # Generate new strings by appending `zero` zeros or `one` ones
#             zero_string = "0" * zero
#             one_string = "1" * one
            
#             good_strings(s + zero_string, low, high, zero, one)
#             good_strings(s + one_string, low, high, zero, one)
        
#         # Initialize the global variable `c`
#         c = 0
#         # Start recursion with an empty string
#         good_strings("", low, high, zero, one)
        
#         # Return the result modulo `10^9 + 7`
#         return c % MOD


# MOD = 10**9 + 7

# class Solution:
#     def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
#         # Memoization dictionary to store the results for specific lengths
#         memo = {}

#         # Helper function to calculate the number of good strings for a given length
#         def dfs(length):
#             # Base case: if length exceeds high, return 0 (invalid)
#             if length > high:
#                 return 0
#             # Base case: if length is within the range [low, high], it's a valid string
#             if length >= low:
#                 return 1
#             # If the result for the current length is already computed, return it from memo
#             if length in memo:
#                 return memo[length]
            
#             # Recursive case: try appending 'zero' 0's or 'one' 1's
#             count = 0
#             count += dfs(length + zero)  # append 'zero' number of '0's
#             count += dfs(length + one)   # append 'one' number of '1's
            
#             # Store the result in the memoization dictionary and return it
#             memo[length] = count % MOD
#             return memo[length]

#         # Start the DFS from length 0
#         return dfs(0)
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
