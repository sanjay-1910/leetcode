class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        
        for word in strs:
            key = ''.join(sorted(word))  # sorted word as key
            
            if key in d:
                d[key].append(word)   # append to list
            else:
                d[key] = [word]      # create new list
        
        return list(d.values())
        