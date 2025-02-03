class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) {
        int inc = 1, dec = 1;
        int currInc = 1, currDec = 1;
        for(int i = 1; i < nums.size(); i++) {
            if(nums[i] > nums[i-1])
                currInc++;
            else {
                inc = max(inc,currInc);
                currInc = 1;
            }
            if(nums[i] < nums[i-1])
                currDec++;
            else {
                dec = max(dec,currDec);
                currDec = 1;
            }
        }
        inc = max(currInc, inc);
        dec = max(currDec, dec);
        return max(inc,dec);   
    }
};