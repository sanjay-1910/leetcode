class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        // int ans = 0;
        // map<string,int>word;
        // for(auto c:words)
        // {
        //     string temp = c;
        //     reverse(c.begin(),c.end());
        //     if(word.find(c) != word.end())
        //     {
        //         ans += 4;
        //         // word.erase(temp);
        //         word.erase(c);
        //     }
        //     else{
        //     if(word.find(temp) == word.end())
        //     {
        //         word[temp] = 1;
        //     }
        //     else
        //     {
        //         word[temp] += 1;
        //     }
        //     }
        // }
        // for (auto &pair : word) {
        // string key = pair.first;
        // if (key.length() >= 2 && key[0] == key[1]) {
        //     ans+=2;
        //     break;
        // } }
        // return ans;
         int ans = 0;
        map<string, int> word;

        for (string& w : words) {
            string rev = w;
            reverse(rev.begin(), rev.end());
            
            if (word[rev] > 0) {
                ans += 4;        // matched a reversible pair
                word[rev]--;     // remove one reverse
            } else {
                word[w]++;       // store for future pairing
            }
        }

        // Check for center (like "aa", "bb", etc.)
        for (auto& p : word) {
            string s = p.first;
            if (s[0] == s[1] && p.second > 0) {
                ans += 2;  // Only one can be placed in the middle
                break;
            }
        }

        return ans;
    }
};