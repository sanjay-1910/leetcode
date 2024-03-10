class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int>v;
        map<int,int>mp;
        map<int,int>mapu;
        for(int i=0;i<nums1.size();i++)
        {
            if(mp.find(nums1[i])==mp.end())
            {
                mp[nums1[i]]=1;
            }
        }
        for(int j=0;j<nums2.size();j++)
        {
            if(mapu.find(nums2[j])==mapu.end())
            {
            if(mp.find(nums2[j])!=mp.end())
            {
                v.push_back(nums2[j]);
            }
                mapu[nums2[j]]=1;
            }
        }
        return v;    
    }
};