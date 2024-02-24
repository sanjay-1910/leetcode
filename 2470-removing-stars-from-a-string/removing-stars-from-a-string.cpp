class Solution {
public:
    string str;
    string removeStars(string s) {
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='*')
            {
                str.pop_back();
            }
            else
            {
                str+=s[i];
            }
        }
        return str;
    }
};