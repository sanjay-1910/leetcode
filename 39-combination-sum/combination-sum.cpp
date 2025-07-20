class Solution {
public:
    vector<vector<int>>final;
    void san(vector<int>&candidates,vector<int>ans,int sum,int target,int index,int size)
    {
        if(sum>target || index>=size)
        {
            return;
        }
        if(sum==target)
        {
            final.push_back(ans);
            return;
        }
        ans.push_back(candidates[index]);
        sum=sum+candidates[index];
        san(candidates,ans,sum,target,index,size);
        ans.pop_back();
        sum=sum-candidates[index];
        san(candidates,ans,sum,target,index+1,size);
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int>ans;
        san(candidates,ans,0,target,0,candidates.size());
        return final;     
    }
};