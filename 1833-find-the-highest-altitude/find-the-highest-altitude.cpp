class Solution {
public:
    int largestAltitude(vector<int>& gain) {
    vector<int>v;
    v.push_back(0);
    for(int i=0;i<gain.size();i++)
    {
        int sum=v.back()+gain[i];
        v.push_back(sum);
    } 
    return *max_element(v.begin(),v.end());
    }
};