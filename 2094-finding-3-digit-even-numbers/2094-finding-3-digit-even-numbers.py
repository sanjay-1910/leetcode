class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits.sort()
        result = set()
        def dp(used, num, length):
            if length == 3:
                if num % 2 == 0:
                    result.add(num)
                return
            for j in range(len(digits)):
                if used[j]:
                    continue
                # Don't allow leading 0
                if length == 0 and digits[j] == 0:
                    continue
                used[j] = True
                dp(used, num * 10 + digits[j], length + 1)
                used[j] = False
        
        used = [False] * len(digits)
        dp(used, 0, 0)
        
        return sorted(result)





















        # a b c
        # a c b
        # b a c
        # b c a
        # c a b
        # c b a
        # 1 2 0 
        # 1 3 0 
        # 1 3 2
        # 1 0 2
        # 2 1 0
        # 2 3 0
        # 3 1 2
        # 3 1 0
        # 3 2 0
        # 3 0 2

        