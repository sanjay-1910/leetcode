class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if(flowerbed.size()==1)
        {
            if(flowerbed[0]==0 && n>1)
            {
            return false;
            }
            else if(flowerbed[0]==1 && n>0)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        for(int i=0;i<flowerbed.size();i++)
        {
          if(i==0)
          {
          if(flowerbed[i]==0 && flowerbed[i+1]==0)
          {
              flowerbed[i]=1;
              n=n-1;
          }
          }
          else if(i==flowerbed.size()-1)
          {
          if(flowerbed[i]==0 && flowerbed[i-1]==0)
          {
              flowerbed[i]=1;
                n=n-1;
          }
          }
          else if(flowerbed[i]==0 && flowerbed[i-1]==0 &&flowerbed[i+1]==0)
          {
              n=n-1;
              flowerbed[i]=1;
          }   
        }
        if(n<=0)
        {
            return true;
        }
        else
        {
            return false;
        }    
        }
};