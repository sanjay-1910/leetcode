class Solution {
public:
    vector<vector<int>>answer;
    void subsets(vector<int>&array,vector<int>&subset,int index,int n)
    {
        if(index == n)
        {
            answer.push_back(subset);
            return;
        }
        subset.push_back(array[index]);
        subsets(array,subset,index+1,n);
        while(index<n-1 && array[index] == array[index+1])
        {
            index += 1;
        }
        subset.pop_back();
        subsets(array,subset,index+1,n);     
    }
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<int>subset;
        sort(nums.begin(),nums.end());
        subsets(nums,subset,0,nums.size());
        return answer;
    }
};