class Solution:
    def small(self,pattern,ans,used,prev_num,index):
        if(index == len(pattern)+1):
            return True
        start = 0
        dec = 0
        end = 0
        if(pattern[index-1] == 'I'):
            prev_num += 1
            dec = 1
            end = len(pattern)+2
        else:
            prev_num -= 1
            dec = -1
            end = 0
        while(prev_num!=end):
            if(used[prev_num]!=False):
                prev_num += dec
                continue
            if(used[prev_num] == False):
                ans.append(prev_num)
                used[prev_num] = True
                if(self.small(pattern,ans,used,prev_num,index+1)):
                    return True
                ans.pop()
                used[prev_num] = False
            prev_num += dec
        return False
    def smallestNumber(self, pattern: str) -> str:
        ans = []
        used = {}
        for i in range(1,len(pattern)+2):
            used[i] = False
        for number in range(1,len(pattern)+2):
            ans = [number]
            used[number] = True
            if(self.small(pattern,ans,used,number,1)):
                result = ''.join(map(str,ans))
                return result
            ans.pop()
            used[number] = False
        return False
                  
        