class Solution:
    def pal(self, s, i, j, memo):
        if i > j:
            return ""
        if i == j:
            return s[i]  # Single character is a palindrome
        
        if (i, j) in memo:
            return memo[(i, j)]
        
        if s[i] == s[j]:
            middle_substring = self.pal(s, i + 1, j - 1, memo)
            if len(middle_substring) == (j - i - 1):  # Ensure it's a valid palindrome
                memo[(i, j)] = s[i] + middle_substring + s[j]
                return memo[(i, j)]
        
        # If not matching, try both possibilities and take the longer one
        pal1 = self.pal(s, i, j - 1, memo)
        pal2 = self.pal(s, i + 1, j, memo)
        
        memo[(i, j)] = pal1 if len(pal1) > len(pal2) else pal2
        return memo[(i, j)]

    def longestPalindrome(self, s: str) -> str:
        memo = {}
        return self.pal(s, 0, len(s) - 1, memo)
