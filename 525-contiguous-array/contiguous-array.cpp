class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;

        vector<int> mp(2*n + 1, INT_MIN);
        mp[0 + n] = -1;

        int sum = 0, maxLength = 0;

        for (int i = 0; i < n; i++) {
            sum += nums[i] ? 1 : -1;

            if (mp[sum + n] == INT_MIN) {
                mp[sum + n] = i;
            }
            else {
                maxLength = max(maxLength, i - mp[sum + n]);
            }
        }

        return maxLength;
    }
};