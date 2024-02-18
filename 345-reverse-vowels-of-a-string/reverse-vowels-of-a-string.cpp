class Solution {
public:
    int isvowel(char s)
    {
        if(s=='a' || s=='e' || s=='i' || s=='o' || s=='u' || s=='A' || s=='E' || s=='I' || s=='O' || s=='U')
        {
            return 1;
        }
        return 0;
    }
    string reverseVowels(string s) {
        int i = 0;
        int j = s.size()-1;
        while(i<=j)
        {
            while(i<=j && isvowel(s[i])!=1)
            {
                i=i+1;
            }
            while(j>=i && isvowel(s[j])!=1)
            {
                j=j-1;
            }
            if(i<=j){
            swap(s[i],s[j]);
            i=i+1;
            j=j-1;
            }
        }
        return s;    
    }
};