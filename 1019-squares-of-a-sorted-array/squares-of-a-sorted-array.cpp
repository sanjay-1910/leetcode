class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int i=0;
        int j=nums.size()-1;
        vector<int>s;
        while(i<=j)
        {
            if(abs(nums[i])<=abs(nums[j]))
            {
                //s.insert(s.begin(),nums[j]**2);
                s.push_back(pow(nums[j],2));
                j=j-1;
            }
            else
            {
                //s.insert(s.begin(),nums[i]**2);
                s.push_back(pow(nums[i],2));

                i=i+1;
            }
        }
        reverse(s.begin(),s.end());
        return s;
    }
};