class Solution {
public:
    int longestValidParentheses(string s) {
        stack<int> st;  // Use a stack to store indices only (char is unnecessary)
        int last_popped = -1;  // Stores the last valid index that was popped
        int answer = 0;         
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                st.push(i);
            } else {  // s[i] == ')'
                if (!st.empty()) {
                    st.pop();  // Match found, pop the stack                  
                    if (!st.empty()) {
                        // If stack is not empty, valid substring is from st.top() to i
                        answer = max(answer, i - st.top());
                    } else {
                        // If stack is empty, valid substring is from last_popped to i
                        answer = max(answer, i - last_popped);
                    }
                } else {
                    // No matching '(' found, update last_popped
                    last_popped = i;
                }
            }
        }
        return answer;
    }
};