class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        w1 = {}
        w2 = {}
        for i in range(0,len(word1)):
            if word1[i] not in w1.keys():
                w1[word1[i]] = 1
            else:
                w1[word1[i]] += 1
            if word2[i] not in w2.keys():
                w2[word2[i]] = 1
            else:
                w2[word2[i]] += 1
        return sorted(w1.values()) == sorted(w2.values()) and w1.keys() == w2.keys()



        