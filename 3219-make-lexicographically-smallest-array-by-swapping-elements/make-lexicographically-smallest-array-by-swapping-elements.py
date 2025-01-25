class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_temp = sorted(nums)
        # nums_temp.sort()
        groups =[]
        group_number = {}
        current_group_number = 0
        current_group = [nums_temp[0]]
        group_number[nums_temp[0]] = current_group_number
        for i in range(1,len(nums_temp)):
            if(nums_temp[i]-nums_temp[i-1] <= limit):
                current_group.append(nums_temp[i])
                group_number[nums_temp[i]] = current_group_number
            else:
                groups.append(current_group)
                current_group  = [nums_temp[i]]
                current_group_number += 1
                group_number[nums_temp[i]] = current_group_number
        groups.append(current_group)
        for j in range(0,len(nums)):
            number = group_number[nums[j]]
            nums[j] = groups[number].pop(0)
        return nums
            
        

