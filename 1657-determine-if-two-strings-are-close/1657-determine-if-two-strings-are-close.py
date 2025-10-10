class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        w1 = {}
        w2 = {}
        l1 = []
        l2 = []
        for i in range(0,len(word1)):
            if word1[i] not in w1.keys():
                w1[word1[i]] = 1
            else:
                w1[word1[i]] += 1
            if word2[i] not in w2.keys():
                w2[word2[i]] = 1
            else:
                w2[word2[i]] += 1
        for key in w1.keys():
            l1.append(w1[key])
        for k in w2.keys():
            l2.append(w2[k])
        l1.sort()
        l2.sort()
        return sorted(w1.values()) == sorted(w2.values()) and set(w1.keys()) == set(w2.keys())



        