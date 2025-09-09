class Solution {
public:
    int isvowel(char s)
    {
        if(s=='a' || s=='e' || s=='i' || s=='o' || s=='u' ||
           s=='A' || s=='E' || s=='I' || s=='O' || s=='U')
        {
            return 1;
        }
        return 0;
    }
    int maxVowels(string s, int k) {
        int c = 0;
        int maxo = 0;
        int i = 0;
        for(int j=0; j<s.size(); j++)
        {
            if(j < k)   // first window
            {
                if(isvowel(s[j]))
                {
                    c += 1;
                }
            }
            else  // sliding part
            {
                if(isvowel(s[j]))
                {
                    c += 1;
                }
                if(isvowel(s[i]))
                {
                    c -= 1;
                }
                i += 1;  // move left pointer only after window full
            }
            maxo = max(maxo, c);
        }
        return maxo;
    }  
};