#include <vector>
#include <string>
class Solution {
    std::vector<std::string> san;

    void sanjay(int open, int close, std::string s, int n) {
        if (open + close >= n * 2) {
            san.push_back(s);
            return;
        } else {
            if (open < n) {
                sanjay(open + 1, close, s + '(', n);
            }
            if (close < open) {
                sanjay(open, close + 1, s + ')', n);
            }
        }
    }

public:
    std::vector<std::string> generateParenthesis(int n) {
        sanjay(1, 0, "(", n);
        return san;
    }
};
