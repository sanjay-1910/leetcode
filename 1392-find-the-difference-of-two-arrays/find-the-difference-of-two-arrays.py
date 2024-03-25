class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1=sorted(list(set(nums1)))
        num2=sorted(list(set(nums2)))
        i=0
        j=0
        l=[]
        m=[]
        n=[]
        while(i<len(num1) and j<len(num2)):
            if num1[i]==num2[j]:
                i=i+1
                j=j+1
            elif num1[i]<num2[j]:
                m.append(num1[i])
                i=i+1
            else:
                n.append(num2[j])
                j=j+1
        if i==len(num1) and j<len(num2):
            n.extend(num2[j: ])
        elif j==len(num2) and i<len(num1):
            m.extend(num1[i: ])
        l.append(m)
        l.append(n)
        return l

        