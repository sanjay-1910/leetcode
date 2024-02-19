class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i=0;
        int j=0;
        while(i<s.size() && j<t.size())
        {
            if(s[i]==t[j])
            {
                i=i+1;
                j=j+1;
            }
            else
            {
                j=j+1;
            }
        }
        if(i<s.size())
        {
            return false;
        }
        else
        {
            return true;
        }
        
    }
};