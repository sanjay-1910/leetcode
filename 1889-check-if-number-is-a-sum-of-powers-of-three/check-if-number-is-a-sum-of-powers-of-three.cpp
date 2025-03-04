#include <cmath> 

class Solution {
public:
    bool check(int n, int power, int sum) {
        int value = pow(3, power);
        
        if (value > n || sum+value > n) {
            return false;
        }
        if (value == n || sum+value == n) {
            return true;
        }

        if (check(n, power + 1, sum+value)) {
            return true;
        }
        if (check(n, power + 1, sum)) {
            return true;
        }
        
        return false;
    }

    bool checkPowersOfThree(int n) {
        return check(n, 0, 0);    
    }
};
