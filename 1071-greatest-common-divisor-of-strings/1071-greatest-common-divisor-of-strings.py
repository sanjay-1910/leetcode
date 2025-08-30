class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2)>len(str1):
            temp=str1
            str1=str2
            str2=temp
        len_str2 = len(str2)
        len_str1 = len(str1)
        for i in range(len_str2, 0, -1):
            if len(str1) % i == 0  and len(str2) % i == 0:
                candidate = str2[:i] * (len_str1 // i)
                crush = str2[:i] * (len_str2 // i)
                if candidate == str1 and crush == str2:
                    return str2[:i]  
        return ""

        