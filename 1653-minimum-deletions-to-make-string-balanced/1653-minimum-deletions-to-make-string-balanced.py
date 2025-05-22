class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        ones = 0
        ans = 0

        for char in s:
            if char == "b":
                ones += 1
            
            elif ones:
                ones -= 1
                ans += 1
        
        return ans 
        