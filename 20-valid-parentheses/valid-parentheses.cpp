class Solution {
public:
    bool isValid(string s) {
        stack<char>st;
        for(int i=0;i<s.size();i++)
        {
            if(st.empty()){
                st.push(s[i]);
            }

            else if(st.top()=='(' and s[i]==')'){
                st.pop();
            }
            else if(st.top()=='[' and s[i]==']'){
                st.pop();
            }
            else if(st.top()=='{' and s[i]=='}'){
                st.pop();
            }
            else
            {
                st.push(s[i]);
            }
            }
        if(!st.empty())
        {
            return false;
        }
        else
        {
        return true;
        }
        
    }
};