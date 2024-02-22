class Solution {
public:
    vector<vector<int>> final;
    
    void san(vector<int>& nums, vector<int>& ans, int k, int index, int le, int n) {
        if (index >=n || le > k) {
            if(le == k){
            final.push_back(ans);
            }
            return;
        }
        if (le == k) {
            final.push_back(ans);
            return;
        }   
        ans.push_back(nums[index]);
        san(nums, ans, k, index + 1, le + 1, n);
        ans.pop_back();
        san(nums, ans, k, index + 1, le, n);
    }
    
    vector<vector<int>> combine(int n, int k) {
        vector<int> nums;
        for (int i = 1; i < n+1; i++) {
            nums.push_back(i);
        }
        vector<int> ans;
        san(nums, ans, k, 0, 0, n);
        return final;
    }
};

