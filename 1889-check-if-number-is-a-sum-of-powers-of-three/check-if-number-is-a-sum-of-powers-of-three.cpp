#include <cmath>

class Solution {
public:
    bool check(int n, int power, int sum) {
        int value = pow(3, power);
        
        if (sum == n) {  // Corrected base case
            return true;
        }
        if (value > n || sum > n) {  
            return false;
        }

        // Take the current power of 3
        if (check(n, power + 1, sum + value)) {
            return true;
        }
        
        // Skip the current power of 3
        if (check(n, power + 1, sum)) {
            return true;
        }

        return false;
    }

    bool checkPowersOfThree(int n) {
        return check(n, 0, 0);
    }
};
