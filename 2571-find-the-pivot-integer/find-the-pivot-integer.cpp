class Solution {
public:
    int pivotInteger(int n) {
        int pre=0;
        int pos=0;
        vector<int>v;
        vector<int>va;
        for(int i=0;i<n;i++)
        {
            pre=pre+(i+1);
            v.push_back(pre);
            pos=pos+(n-i);
            va.push_back(pos);
        }
        reverse(va.begin(),va.end());
        for(int i=0;i<n;i++)
        {
            if(v[i]==va[i])
            {
                return i+1;
            }
        }
        return -1;
    }
};