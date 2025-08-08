class Solution {
public:
    // vector< vector <int> >v;
    void Ram(vector< vector <int> >&v,int start,vector<int>&nums,int end)
    {
        if(start>=end)
        {
           v.push_back(nums);
           return; 
        }
        for(int i = start ; i <= end ; i++){
            swap(nums[start],nums[i]);
            Ram(v,start+1,nums,end);
            swap(nums[start],nums[i]);
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector< vector <int> >v;
        Ram(v,0,nums,nums.size()-1);
        return v;
    }
};