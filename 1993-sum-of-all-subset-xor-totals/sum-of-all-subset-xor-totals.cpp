class Solution {
public:
    int solve(vector<int>& nums,int i,int sum){
        if(i==nums.size()){
            return sum;
        }
        int include=solve(nums,i+1,sum^nums[i]);
        int exclude=solve(nums,i+1,sum);
        return include+exclude;
    }
    int subsetXORSum(vector<int>& nums) {
        return solve(nums,0,0);
    }
};