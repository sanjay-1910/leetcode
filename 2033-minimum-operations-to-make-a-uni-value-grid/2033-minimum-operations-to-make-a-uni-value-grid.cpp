class Solution {
public:
    int minOperations(vector<vector<int>>& grid, int x) {
        vector<int>arr;
        for(int i = 0 ; i < grid.size() ; i++){
            for(int j = 0 ; j < grid[0].size() ; j++){
                arr.push_back(grid[i][j]);
            }
        }
        int n = arr.size();
        sort(arr.begin(),arr.end());
        int finalCommonNumber = arr[n/2];   // median for minimum operations.
        int res = 0;
        for(int num : arr){
            if(num % x != finalCommonNumber % x)   return -1;
            res += abs(finalCommonNumber - num) / x;
        }
        return res;
    }
};