/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    int parseInt(string &traversal, int &i) {
        int n = traversal.length();
        int res = 0;
        while(i < n && traversal[i] != '-'){
            res = res*10 + (traversal[i] - '0');
            i++;
        }
        return res;
    }

    int parseLevel(string &traversal, int &i) {
        int n = traversal.length();
        int level = 0;
        while(i < n && !(traversal[i] >= '0' && traversal[i] <= '9')) {
            level++;
            i++;
        }
        return level;
    }

public:
    TreeNode* recoverFromPreorder(string traversal) {
        int n = traversal.length();
        int i = 0;

        TreeNode *root = new TreeNode(parseInt(traversal, i));

        stack<pair<TreeNode*, int>> stk;
        stk.push({root, 0});
        while(i < n) {
            int currLevel = parseLevel(traversal, i);
            int val = parseInt(traversal, i);

            while(!stk.empty() && stk.top().second >= currLevel) {
                stk.pop();
            }

            if(!stk.empty()) {
                TreeNode* newNode = new TreeNode(val);
                if(stk.top().first->left == NULL) {
                    stk.top().first->left = newNode;
                } else {
                    stk.top().first->right = newNode;
                }
                stk.push({newNode, currLevel});
            }
        }

        return root;
    }
};