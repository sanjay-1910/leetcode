class Solution {
public:
    int rob(vector<int>& arr) {
        int prev = arr[0];
        int prev2 = 0;
        for(int i=1;i<arr.size();i++)
        {
            int pick = arr[i] + prev2;
            int non_pick = prev;
            int current = max(pick,non_pick);
            prev2 = prev;
            prev = current;
            
        }
        return prev;
        
    }
};