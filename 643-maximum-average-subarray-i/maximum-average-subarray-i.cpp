class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        int i=0;
        int j=0;
        double s=0;
        double max=INT_MIN;
        while(j<nums.size())
        {
            if(j<k-1)
            {
                s=s+nums[j];
                j=j+1;
            }
            else
            {
                s=s+nums[j];
                if(s>max)
                {
                    max=s;
                }
                s=s-nums[i];
                i=i+1;
                j=j+1;
            }
        }
        return (max/k);    
    }
};