class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = []
        prefix_array = []
        suffix_array = []
        prefix = 0
        suffix = 0
        zero_index_operations = 0
        # last_index_operations = 0
        for i in range(0,len(boxes)):
            if(boxes[i] == '1'):
                prefix += 1
            prefix_array.append(prefix)
            # if(i<len(boxes)-1 and boxes[i] == '1'):
            #     last_index_operations += (len(boxes)-i-1)
            if(boxes[n-i-1] == '1'):
                suffix += 1
            suffix_array.append(suffix)
        suffix_array.reverse()
        for k in range(1,len(boxes)):
            # if(suffix_array[k] == '1'):
            #     suffix_array -= 1
            zero_index_operations += suffix_array[k]
        answer.append(zero_index_operations)
        prefix_sum = 0
        for j in range(1,len(boxes)):
            operations = 0
            # operations = (last_index_operations+prefix_array[j])
            if(boxes[j] == '1'):
                # zero_index_operations -= 1
                prefix_array[j] -= 1
            zero_index_operations = (zero_index_operations-suffix_array[j])
                # prefix_array[j] -= 1
            operations += zero_index_operations
            prefix_sum += prefix_array[j]
            operations += prefix_sum
            answer.append(operations)
        # answer.append(last_index_operations)
        return answer
        

        
        