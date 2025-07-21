class Solution {
public:
    string makeFancyString(string s) {
        string ans = "";
        ans += s[0];
        int c = 1;
        char prev = s[0];
        for(int i=1;i<s.size();i++)
        {
            if(s[i] == prev)
            {
                if(c<2)
                {
                    ans += s[i];
                    c+=1;
                }
            }
            else{
                ans += s[i];
                c = 1;
                prev = s[i];
            }
        }
        return ans;
        
    }
};