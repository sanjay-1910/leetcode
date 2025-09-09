class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        sort(nums.begin(),nums.end());
        int i=0;
        int c=0;
        int j=nums.size()-1;
        while(i<=j && nums.size()>0)
        {
            if(nums[i]+nums[j]==k && i!=j)
            {
                c=c+1;
                i=i+1;
                j=j-1;
            }
            else if(nums[i]+nums[j]>k)
            {
                j=j-1;
            }
            else
            {
                i=i+1;
            }
        }
        return c;   
    }
};