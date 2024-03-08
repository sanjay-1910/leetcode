class Solution {
public:
    int maxFrequencyElements(vector<int>& nums) {
        map<int,int>mp;
        int max=0;
        int c=0;
        for(int i=0;i<nums.size();i++)
        {
            mp[nums[i]]++;
        }
        for(auto it :mp)
        {
            if(it.second>max)
            {
                max=it.second;
                c=it.second;
            }
            else if(it.second==max)
            {
                c=c+it.second;
            }
        }
        return c;
        
    }
};