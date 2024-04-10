class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        deque<int>dq;
        int n=deck.size();
        sort(deck.begin(),deck.end());
        vector<int>ans(n);
        for(int i=0;i<n;i++)
        {
            dq.push_back(i);
        }
        for(int i=0;i<deck.size();i++)
        {
            ans[dq.front()]=deck[i];
            dq.pop_front();
            if(!dq.empty())
            {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
        return ans;

        
    }
};