class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        vector<string> res;
        int n = nums.size();
        if (n == 0) return res;

        int start = 0;  // Pointer to track the start of a range

        for (int i = 0; i < n; i++) {
            // If it's the last element or the sequence breaks
            if (i == n - 1 || nums[i] + 1 != nums[i + 1]) {
                if (start == i) {
                    res.push_back(to_string(nums[start]));  // Single element case
                } else {
                    res.push_back(to_string(nums[start]) + "->" + to_string(nums[i]));
                }
                start = i + 1;  // Move start to the next potential range
            }
        }

        return res;
    }
};