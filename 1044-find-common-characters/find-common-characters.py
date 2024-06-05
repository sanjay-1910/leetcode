class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d = {}
        for char in words[0]:
            d[char] = d.get(char, 0) + 1

        # Intersect with counts from subsequent words
        for word in words[1:]:
            e = {}
            for char in word:
                if char in d:
                    e[char] = e.get(char, 0) + 1
            # Update d to keep the minimum counts
            for char in d:
                if char in e:
                    d[char] = min(d[char], e[char])
                else:
                    d[char] = 0

        # Build the result list from the count dictionary
        result = []
        for char, count in d.items():
            result.extend([char] * count)
        
        return result
            


        
        
                                                       
        