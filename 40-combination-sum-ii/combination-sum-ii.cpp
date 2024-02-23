class Solution {
public:
    vector<vector<int>>final;
    void san(vector<int>candidates,vector<int>&ans,int index,int target,int size,int sum)
    {
        if(sum>=target)
        {
        if(sum==target)
        {
            final.push_back(ans);
            return;
        }
            return;
        }
        if(index>=size)
        {
            return;
        }
        ans.push_back(candidates[index]);
        san(candidates,ans,index+1,target,size,sum+candidates[index]);
        while(index+1<size && candidates[index] == candidates[index+1])
        {
            index++;
        }
        ans.pop_back();
        san(candidates,ans,index+1,target,size,sum);
    } 
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        vector<int>ans;
        //final.clear();
        sort(candidates.begin(),candidates.end());
        san(candidates,ans,0,target,candidates.size(),0);
        return final; 
    }
};
