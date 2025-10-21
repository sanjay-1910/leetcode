class Solution {
    public int longestSubarray(int[] nums) {
        int prev = 0;
        int curr = 0;
        int ans = 0;
        int flag = 0;
        for(int i=0;i<nums.length;i++)
        {
            if(nums[i] == 1)
            {
                curr += 1;
            }
            else
            {
                ans = Math.max(ans,prev+curr);
                prev = curr;
                curr = 0;
                flag = 1;
            }
        }
        ans = Math.max(ans,prev+curr);
        if(flag == 0)
        {
            return nums.length-1;
        }
        return ans;
        
    }
}