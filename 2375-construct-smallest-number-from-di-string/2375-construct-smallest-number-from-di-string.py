class Solution:
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        stack = []

        for i in range(len(pattern) + 1):
            stack.append(str(i + 1))   # push the next number
            if i == len(pattern) or pattern[i] == "I":
                while stack:
                    ans.append(stack.pop())

        return "".join(ans)

                


                  
        