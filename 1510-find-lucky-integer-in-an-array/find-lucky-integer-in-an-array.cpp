class Solution {
public:
    int findLucky(vector<int>& arr) {
        map<int,int>mp;
        for(int i=0;i<arr.size();i++)
        {
            if(mp.find(arr[i]) == mp.end())
            {
                mp[arr[i]] = 1;
            }
            else
            {
                mp[arr[i]] += 1;
            }
        }
    int ans = -1;
    for (auto it : mp) 
    {
        if (it.first == it.second) 
        {
            ans = max(ans, it.first);
        }
    }
    return ans;
    }
};