class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        front_dic = {}
        back_dic = {}
        left_dominant = -1
        right_dominant = -1
        left = []
        right = []
        for i in range(0,len(nums)):
            if(nums[i] not in front_dic):
                front_dic[nums[i]] = 1
            else:
                front_dic[nums[i]] += 1
            if(front_dic[nums[i]] > (i+1)/2):
                left_dominant = nums[i]
                left.append(left_dominant)
            elif(front_dic[left_dominant] > (i+1)/2):
                left.append(left_dominant)
            else:
                left.append(-1)
            k = -(i+1)
            if(nums[k] not in back_dic):
                back_dic[nums[k]] = 1
            else:
                back_dic[nums[k]] += 1
            if(back_dic[nums[k]] > (i+1)/2):
                right_dominant = nums[k]
                right.append(right_dominant)
            elif(back_dic[right_dominant] > (i+1)/2):
                right.append(right_dominant)
            else:
                right.append(-1)
        right.reverse()
        for index in range(0,len(nums)-1):
            if(left[index] == right[index+1]):
                return index
        return -1


            
            

            


        
            
        