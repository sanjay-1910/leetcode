class Solution {
public:
    int maxArea(vector<int>& height) {
        int i=0;
        int j=height.size()-1;
        int ma=0;
        while(i<j)
        {
            int wi=j-i;
            if(height[i]<height[j])
            {
                int re=wi*height[i];
                if(ma<re)
                {
                    ma=re;
                }
                i=i+1;
            }
            else
            {
                int re=wi*height[j];
                if(ma<re)
                {
                    ma=re;
                }
                j=j-1;
            }
        }
        return ma;  
    }
};