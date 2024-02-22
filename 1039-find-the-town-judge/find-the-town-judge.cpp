class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        if(n==1)
        {
            return 1;
        }
        map<int,int>mp;
        map<int,int>val;
        int ans=-1;
        int c=0;
        if(trust.size()<n-1)
        {
            return -1;
        }
        else
        {
            for(int i=0;i<trust.size();i++)
            {
                if(mp.find(trust[i][1])==mp.end())
                {
                    mp[trust[i][1]]=1;
                }
                else
                {
                    mp[trust[i][1]]=mp[trust[i][1]]+1;
                } 
                if(val.find(trust[i][0])==val.end())
                {
                    val[trust[i][0]]=1;
                } 
                else
                {
                 val[trust[i][0]]+=1;   
                }
            }
        }
        for(auto it:mp)
        {
            if(it.second==n-1)
            {
                c=c+1;
                ans=it.first;
            }
        }
        if(c==1)
        {
            if(val.find(ans)==val.end())
            {
            return ans;
            }
            else
            {
                return -1;
            }
        }
        else
        {
            return -1;
        }
    return 0;
}
};