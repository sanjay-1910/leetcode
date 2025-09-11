class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i=0
        j=0
        c=0
        ans = 0
        while(j<len(nums)):
            if nums[j]==0:
                if c<k:
                    c+=1
                else:
                    while(nums[i] !=0):
                        i+=1
                    i+=1
            ans = max(ans,j-i+1)
            j+=1
        return ans

            
            

            

            


        